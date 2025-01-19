# Generative-AI-Powered-Resume-Analyzer

Here's the documentation for your **Generative AI-Powered Resume Analyzer** in Markdown format. You can save it as a `README.md` file or convert it into a PDF as needed.

---

# Generative AI-Powered Resume Analyzer

## Overview
This project automates the process of extracting, analyzing, and scoring resume data using advanced Generative AI techniques. It processes resumes in **PDF format**, extracts key information, and outputs the results into a neatly formatted **Excel sheet**. The solution leverages the power of Natural Language Processing (NLP) for high accuracy and scalability, meeting the demands of modern recruitment processes.

---

## Key Features
### 1. **Generative AI Integration**
- Utilized **Hugging Face Transformers** (NER Pipeline with `dbmdz/bert-large-cased-finetuned-conll03-english`) to extract:
  - Candidate names (context-aware).
  - Educational institutions (universities, colleges, etc.).
  - Other key entities like skills, courses, and disciplines.
- Implemented context-aware **Generative AI scoring** for:
  - **Gen AI Experience**: Based on exposure to advanced technologies (e.g., Generative AI, GPT).
  - **AI/ML Experience**: Based on hands-on experience with Machine Learning frameworks (e.g., TensorFlow, Keras).

### 2. **Batch Processing**
- Efficiently processes **multiple resumes** in a directory.
- Handles **up to 100 resumes** at once, ensuring timely output generation for large datasets.

### 3. **Field-Specific Refinement**
- **Regex Optimization**:
  - Extracts structured data for fields such as contact details, year of study, CGPA, and skills.
- **Fallback Logic**:
  - Handles varying resume formats to minimize "Not Found" entries.

### 4. **Scalability & Innovation**
- Designed for **scalable use** with additional support for future improvements, including:
  - Integration with cloud platforms like AWS or Google Cloud for large-scale resume parsing.
  - Extending functionality to include career role match scores or inferred career potential.
- Innovative features:
  - Scoring mechanism (1-3) for Generative AI and AI/ML experience.
  - Extraction of **supporting information** like certifications, projects, and internships for added insights.

---

## Approach

### **Step 1: Resume Text Extraction**
- Used **PyMuPDF (fitz)** to extract raw text from PDF resumes, handling multiple pages seamlessly.

### **Step 2: Entity Extraction**
- **Generative AI (NER)**:
  - Extracted contextually relevant entities like `Name` and `University` using an NER pipeline.
- **Regex Refinement**:
  - Extracted specific details like `Contact Details`, `Year of Study`, `Course`, and `CGPA`.

### **Step 3: Scoring Mechanism**
- Assigned **Gen AI Experience Score**:
  - `3`: Worked on advanced areas such as Agentic RAG or Generative AI.
  - `2`: Hands-on experience with Deep Learning frameworks.
  - `1`: Basic exposure to Generative AI concepts.
- Assigned **AI/ML Experience Score**:
  - `3`: Proficient with TensorFlow, Keras, or equivalent frameworks.
  - `2`: Hands-on knowledge of AI/ML basics.
  - `1`: Basic understanding or theoretical knowledge.

### **Step 4: Batch Processing**
- Processed all resumes in the given directory, ensuring efficient and parallelized execution for large datasets.

### **Step 5: Output to Excel**
- Compiled extracted data into a neatly formatted **Excel sheet** with the following fields:
  - **Name**
  - **Contact Details**
  - **University**
  - **Year of Study**
  - **Course**
  - **Discipline**
  - **CGPA/Percentage**
  - **Key Skills**
  - **Gen AI Experience Score**
  - **AI/ML Experience Score**
  - **Supporting Information**

---


## Technical Details
### **Technologies Used**
1. **Programming Language**:
   - Python
2. **Libraries and Frameworks**:
   - **PyMuPDF (fitz)**: PDF text extraction.
   - **Hugging Face Transformers**: NER pipeline for entity extraction.
   - **pandas**: Data organization and Excel output.
   - **re**: Regex for additional text parsing.

### **Challenges Addressed**
- **Inconsistent Resume Formats**:
  - Combined NER and regex for robust data extraction.
- **Scalability**:
  - Optimized for processing batches of resumes with minimal overhead.
- **Accuracy**:
  - Leveraged Generative AI to complement regex-based methods for higher accuracy.

---

## How to Run
### **Pre-requisites**
1. Install dependencies:
   ```bash
   pip install pandas transformers pymupdf
   ```
2. Ensure all resumes are stored in a directory (e.g., `path/to/resumes`).

### **Steps to Execute**
1. Run the script:
   ```bash
   python resume_analyzer.py
   ```
2. Provide the directory path for input resumes and the desired output Excel file path.

3. View the results in the output Excel file.

---

## Future Enhancements
1. **Cloud Integration**:
   - Add cloud storage support (e.g., Google Drive, AWS S3) for large-scale resume processing.
2. **Role Matching**:
   - Include a matching score for job roles based on skills and experience.
3. **Advanced Insights**:
   - Add inferred career potential and detailed analysis for recruiters.

---

## Conclusion
This solution demonstrates the power of **Generative AI** in automating and improving resume analysis, providing accurate, scalable, and innovative insights for modern recruitment needs.

---

Let me know if you need any further refinements!
