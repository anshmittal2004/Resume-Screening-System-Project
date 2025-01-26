# AI-Based Resume Screening System

This project is a Flask-based web application designed to automate resume screening using Natural Language Processing (NLP). It analyzes resumes uploaded as PDFs, extracts relevant skills and keywords, and calculates a match score based on predefined criteria.

## Features

- Extracts text from PDF resumes.
- Uses SpaCy NLP to identify skills, keywords, and relevant entities.
- Compares extracted skills with a predefined set of desired keywords.
- Calculates a match score and displays matched keywords, extracted skills, and other relevant information.
- Provides a user-friendly interface for uploading resumes and viewing results.

## Technologies Used

- **Backend**: Python, Flask
- **NLP**: SpaCy (`en_core_web_sm` model)
- **File Processing**: PyPDF2
- **Frontend**: HTML, CSS (custom styling for a modern UI)
- **Server**: Flask development server

## How It Works

1. **Upload Resume**: The user uploads a resume in PDF format.
2. **Text Extraction**: The app extracts text from the PDF using PyPDF2.
3. **NLP Processing**: Extracts skills and relevant entities using SpaCy.
4. **Keyword Matching**: Compares extracted skills to a predefined list of desired skills/keywords.
5. **Score Calculation**: Calculates a match score and highlights matched keywords.
6. **Result Display**: Displays the score, matched keywords, and extracted skills in a user-friendly format.

## Predefined Keywords

Some of the predefined keywords the system matches against include:

- **Programming Languages**: Python, C++, Java, JavaScript, SQL, etc.
- **Frameworks & Tools**: Flask, Docker, Kubernetes, React, Node.js, etc.
- **Skills**: Machine Learning, Data Analysis, NLP, Cloud Computing, etc.

The full list can be customized in the `KEYWORDS` array in `app.py`.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anshmittal2004/AI-Based-Resume-Screening-System.git
   cd AI-Based-Resume-Screening-System
2.  pip install flask spacy PyPDF2
python -m spacy download en_core_web_sm
3.  Run the Application:
python app.py
4.  Access the Application: Open your browser and navigate to http://127.0.0.1:5000.

Usage
Open the application in your browser.
Upload a PDF resume using the upload form.
View the calculated match score, matched keywords, and extracted skills.
Screenshots
Home Page
A user-friendly form for uploading resumes.


Result Page
Displays match score, matched keywords, and extracted skills.


File Structure
app.py: Main application logic.
templates/index.html: HTML template for the web interface.
static/style.css: Custom CSS for styling the interface.


Customization
Modify the KEYWORDS array in app.py to update the list of desired skills/keywords.
Customize the HTML and CSS in templates/index.html and static/style.css to change the interface.


Future Enhancements
Add support for other resume formats (e.g., DOCX).
Implement user authentication for saving and viewing results.
Enhance the scoring algorithm for better accuracy.
Add a database to store resumes and results for future reference.
