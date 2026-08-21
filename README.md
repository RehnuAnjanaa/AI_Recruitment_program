# AI_Recruitment_program
Helps to classify skills of your resume
AI Recruiter is a Python-based recruitment assistance project that uses basic Natural Language Processing (NLP) concepts to extract skills from conversational text and resumes.

The project is divided into two main parts:

Part 1 – Conversational Skill Extraction:
The system accepts conversational input from a user and extracts relevant:

Skills
Technologies
Programming languages

The extracted information is organized and displayed in JSON format.

Part 2 – Candidate Matching: 
The system extends Part 1 by automatically:

Extracting skills from resume text
Suggesting suitable job roles based on candidate skills
Matching candidates with job descriptions
Identifying matched and missing skills
Calculating a candidate-job match score

Technologies Used
Python
JSON
Basic NLP concepts
Project Structure


AI_Recruiter/
├── main.py
├── resume_extractor.py
├── job_matcher.py
└── README.md

How to Run:
Run Part 1:
python main.py

Run resume extraction and role suggestions:
python resume_extractor.py



Input:
I have experience with Python, Machine Learning and TensorFlow.

Output:
Suggested Role: Machine Learning Engineer
Match Score: 75%
Matched Skills: Python, Machine Learning, TensorFlow


Future Improvements:
Support for PDF and DOCX resumes
Larger skill database
Advanced NLP and AI-based extraction
RAG Recruiter using Ollama and Llama
