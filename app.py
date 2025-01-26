from flask import Flask, request, render_template
import PyPDF2


import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")  # Load SpaCy's English model.

# Define a list of desired skills or keywords.
KEYWORDS = ["Python", "Machine Learning", "Flask", "API", "Data Analysis", "NLP", "Cloud Computing","Docker",
            "C++","C","Java","SQL","Data Structure","Algorithm","DBMS","Computer Networks","Communication",
            "Javascript","HTML","CSS","Developed","DevOPs","Deep Learning","Kubernetes","software","Node.js",
            "GitHub","Programming","Flutter","experience","EDUCATION","Skills","Technical","Cloud","Google"
            "Internship","education","Certification","courseera","Deployment","MongoDb","LinkedIn","Typescript"
            "CGPA","React","Intern","project","professionals","Server","startup"
            ]

# Function to extract text from a PDF file.
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract skills/entities from the resume text using NLP.
def extract_skills_with_nlp(resume_text):
    doc = nlp(resume_text)
    extracted_skills = set()
    for token in doc:
        # Check for proper nouns, nouns, or entities related to skills/technologies.
        if token.pos_ in ["PROPN", "NOUN"] or token.ent_type_ in ["ORG", "PRODUCT"]:
            extracted_skills.add(token.text)
    return extracted_skills

# Function to calculate the match score between extracted skills and predefined keywords.
def calculate_score_nlp(extracted_skills, keywords):
    matched_keywords = [kw for kw in keywords if kw.lower() in [skill.lower() for skill in extracted_skills]]
    score = (len(matched_keywords) / len(keywords)) * 100
    return matched_keywords, round(score, 2)

# Flask route to handle form submission and processing.
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["resume"]
        if uploaded_file.filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)  # Extract text from PDF.
            extracted_skills = extract_skills_with_nlp(resume_text)  # Extract skills using NLP.
            matched_keywords, score = calculate_score_nlp(extracted_skills, KEYWORDS)  # Calculate score.
            
            return render_template("index.html", score=score, matched_keywords=matched_keywords, extracted_skills=extracted_skills)
        else:
            return render_template("index.html", error="Please upload a PDF file.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
