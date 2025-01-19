import os
import re
import pandas as pd
import fitz  # PyMuPDF for PDF parsing
from transformers import pipeline
from tqdm import tqdm

# Initialize transformer-based NER pipeline
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Mandatory columns to extract
MANDATORY_COLUMNS = [
    "Name", "Contact Details", "University", "Year of Study", "Course", "Discipline",
    "CGPA/Percentage", "Key Skills", "Gen AI Experience Score", "AI/ML Experience Score",
    "Supporting Information"
]

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    return text

# Extract Name and University using NER
def extract_name_and_university(text):
    """Extract name and university using NER."""
    entities = ner_pipeline(text)
    name = "Not found"
    university = "Not found"
    
    for entity in entities:
        if entity['entity'] == 'B-PER' and name == "Not found":
            name = entity['word']
        elif entity['entity'] == 'B-ORG' and university == "Not found":
            university = entity['word']
    
    return name, university

# Extract email and phone
def extract_contact_details(text):
    """Extract email and phone number from the text."""
    email = re.search(r'\S+@\S+', text)
    phone = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return {
        "Email": email.group() if email else "Not found",
        "Phone": phone.group() if phone else "Not found"
    }

# Extract year of study and course
def extract_year_and_course(text):
    """Extract year of study and course using regex."""
    year = re.search(r'\b(19|20)\d{2}\b', text)
    course = re.search(r'(B\.?Tech|M\.?Tech|Bachelor|Master|Engineering|Science|Arts)', text, re.IGNORECASE)
    return {
        "Year of Study": year.group() if year else "Not found",
        "Course": course.group() if course else "Not found"
    }

# Extract CGPA/Percentage
def extract_cgpa_or_percentage(text):
    """Extract CGPA or Percentage using regex."""
    cgpa = re.search(r'CGPA[:\s]*([0-9]+(?:\.[0-9]+)?)', text)
    percentage = re.search(r'(\d{1,3}(?:\.\d+)?%)', text)
    return cgpa.group(1) if cgpa else (percentage.group(1) if percentage else "Not found")

# Extract skills
def extract_skills(text):
    """Extract skills from predefined keywords."""
    skills_keywords = ['Machine Learning', 'AI', 'Python', 'Data Science', 'TensorFlow', 'Keras', 'NLP', 'Generative AI']
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return ", ".join(found_skills) if found_skills else "Not found"

# Calculate Generative AI and AI/ML Experience Score
def calculate_experience_scores(text):
    """Calculate experience scores based on text analysis."""
    gen_ai_score = 1
    ai_ml_score = 1
    
    if 'agentic' in text.lower() or 'rag' in text.lower():
        gen_ai_score = 3
    elif 'hands-on' in text.lower() or 'project' in text.lower():
        gen_ai_score = 2
    
    if 'advanced' in text.lower() or 'deep learning' in text.lower():
        ai_ml_score = 3
    elif 'machine learning' in text.lower():
        ai_ml_score = 2

    return gen_ai_score, ai_ml_score

# Extract supporting information
def extract_supporting_info(text):
    """Extract certifications, internships, or project details."""
    certifications = re.findall(r'(certified|certification|course|internship|project)', text, re.IGNORECASE)
    return ", ".join(certifications) if certifications else "Not found"

# Process a single resume
def process_resume(pdf_path):
    """Process a single resume and extract key details."""
    text = extract_text_from_pdf(pdf_path)
    
    name, university = extract_name_and_university(text)
    contact_details = extract_contact_details(text)
    year_and_course = extract_year_and_course(text)
    cgpa_percentage = extract_cgpa_or_percentage(text)
    skills = extract_skills(text)
    gen_ai_score, ai_ml_score = calculate_experience_scores(text)
    supporting_info = extract_supporting_info(text)
    
    return {
        "Name": name,
        "Contact Details": f"Email: {contact_details['Email']}, Phone: {contact_details['Phone']}",
        "University": university,
        "Year of Study": year_and_course["Year of Study"],
        "Course": year_and_course["Course"],
        "Discipline": "Not found",  # Placeholder as discipline extraction needs custom logic
        "CGPA/Percentage": cgpa_percentage,
        "Key Skills": skills,
        "Gen AI Experience Score": gen_ai_score,
        "AI/ML Experience Score": ai_ml_score,
        "Supporting Information": supporting_info
    }

# Process all resumes in a folder
def process_resumes(folder_path):
    """Batch process all resumes in a folder."""
    all_data = []
    for file in tqdm(os.listdir(folder_path), desc="Processing Resumes"):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file)
            resume_data = process_resume(pdf_path)
            all_data.append(resume_data)
    return all_data

# Save results to Excel
def save_to_excel(data, output_file):
    """Save extracted data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

# Main script
if __name__ == "__main__":
    folder_path = r"C:\Users\Rahul\OneDrive\Desktop\resume_analyzer\resumes"  # Replace with your folder containing PDFs
    output_file = "extracted_resume_data.xlsx"
    
    resume_data = process_resumes(folder_path)
    save_to_excel(resume_data, output_file)

