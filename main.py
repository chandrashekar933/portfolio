from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

app = FastAPI(title="My Portfolio")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


PROFILE = {
    "name": "Parmati Chandra Shekar",
    "short_name": "Chandra Shekar",
    "photo": "",  
    "title": "Aspiring Software Engineer | AI/ML | Python, Java and Backend APIs",
    "location": "Hyderabad, India",
    "availability": "Available immediately",
    "email": "chandup223344@gmail.com",
    "phone": "+91-9866242581",
    "phone_link": "+919866242581",  # digits only, used for the tel: link
    "github": "https://github.com/chandrashekar933",
    "summary": (
        "B.Tech Computer Science (AI & ML) graduate with hands-on project experience in "
        "machine learning, deep learning, NLP and backend development. Comfortable building "
        "end-to-end solutions in Python and Java, exposing them through Django and FastAPI, "
        "and packaging them with Docker. Currently deepening full-stack skills "
        "(JavaScript, HTML/CSS) and cloud-native tooling. Seeking a graduate software "
        "or AI/ML engineering role."
    ),
}

SKILL_GROUPS = [
    ("Languages", ["Python", "Java", "SQL", "JavaScript", "HTML", "CSS"]),
    ("AI / ML", ["Machine Learning", "Deep Learning", "Generative AI", "NLP", "Computer Vision"]),
    ("Backend & APIs", ["Django", "FastAPI", "REST APIs"]),
    ("Libraries", ["Pandas", "NumPy", "TensorFlow", "PyTorch", "SpaCy"]),
    ("Cloud & DevOps", ["Docker", "Kubernetes", "CI/CD", "AWS", "Git", "GitHub"]),
    ("Databases", ["MySQL"]),
    ("Concepts", ["Object-Oriented Programming"]),
]

PROJECTS = [
    {
        "title": "Automated Detection of Spinal Lesions from CT Scans via Deep Transfer Learning",
        "blurb": "Deep learning model that classifies vertebrae in CT scans as normal or lesion-containing.",
        "tech": ["Python", "TensorFlow", "VGG19", "Deep Learning"],
        "bullets": [
            "Built a deep learning model on a pre-trained VGG19 network to classify vertebrae in CT scan images as normal or lesion-containing.",
            "Fine-tuned the pre-trained weights to work with a limited medical dataset, reusing learned features instead of training from scratch.",
            "Prepared image preprocessing and augmentation steps to improve how well the model generalizes.",
        ],
        "url": "",  # add a GitHub link here if you publish this project
    },
    {
        "title": "AI-Based CV Screening and Ranking System",
        "blurb": "NLP pipeline that extracts skills from CVs and ranks candidates against a job description.",
        "tech": ["Python", "NLP", "Machine Learning", "SpaCy", "TF-IDF"],
        "bullets": [
            "Built an NLP pipeline that extracts skills and experience from candidate CVs and ranks candidates by relevance to a job description.",
            "Applied tokenization, stopword removal and TF-IDF vectorization to turn raw resume text into features for ranking.",
            "Produces a ranked shortlist so recruiters can review the best matches first instead of screening every CV by hand.",
        ],
        "url": "https://github.com/chandrashekar933/AI-Resume-screening",
    },
    {
        "title": "Smart Banking System with Real-Time Fraud Detection",
        "blurb": "Java banking app with REST endpoints and fraud detection on transaction patterns.",
        "tech": ["Java", "MySQL", "REST APIs", "HTML", "CSS", "JavaScript"],
        "bullets": [
            "Built a Java banking application with REST-style endpoints, MySQL storage and a browser front end for accounts and transactions.",
            "Implemented fraud detection logic using Graph DFS, a Priority Queue and a Sliding Window to flag suspicious transaction patterns.",
            "Organized the code into model, server and service layers to keep responsibilities separate and the project easy to extend.",
        ],
        "url": "https://github.com/chandrashekar933/Smart-Banking-System",
    },
]

# Smaller repos, shown as simple links on the Projects page.
MORE_REPOS = [
    {"title": "Spam Email Classifier", "note": "Spam detection using TF-IDF and Naive Bayes (Python).",
     "url": "https://github.com/chandrashekar933/spam-email-classifier"},
    {"title": "Personalized Learning Recommendation", "note": "Python project.",
     "url": "https://github.com/chandrashekar933/Personalized-Learning-Recommendation"},
    {"title": "Movie Ticket Booking", "note": "Python project.",
     "url": "https://github.com/chandrashekar933/movie_ticket_booking"},
    {"title": "FastAPI Practice", "note": "My FastAPI learning projects.",
     "url": "https://github.com/chandrashekar933/fastapi"},
]

EDUCATION = [
    {
        "school": "Guru Nanak Institute of Technology, Hyderabad, India",
        "degree": "B.Tech in Computer Science and Engineering (AI & ML)",
        "period": "October 2022 – June 2026",
        "extra": "Relevant modules: Machine Learning, Deep Learning, Neural Networks, DBMS",
    },
    {"school": "TSWRIES", "degree": "Intermediate (Class XII)", "period": "2022", "extra": ""},
    {"school": "Lotus High School", "degree": "Secondary Education (Class X)", "period": "2020", "extra": ""},
]



@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request, "index.html",
        {
            "profile": PROFILE,
            "projects": PROJECTS,
            "more_repos": MORE_REPOS,
            "skill_groups": SKILL_GROUPS,
            "education": EDUCATION,
        },
    )
