"""Views for the cv app.

All CV content lives here as Python data. The templates never contain
CV text directly; they only decide WHERE each piece of data goes.
"""
from datetime import date

from django.shortcuts import render

# Contact details are shared by both pages, so they live in one place.
PERSON = {
    "name": "Bat-Orgil Tsend-Ochir",
    "phone": "(917) 701-1612",
    "email": "bt2291@nyu.edu",
    "links": [
        {"label": "LinkedIn", "url": "https://linkedin.com/in/bat-orgil-tsend-ochir"},
        {"label": "GitHub", "url": "https://github.com/batorgillts"},
    ],
}

EDUCATION = [
    {
        "school": "New York University Tandon School of Engineering",
        "degree": "M.S. in Computer Science",
        "location": "New York, USA",
        "start": date(2026, 9, 1),
        "end": date(2028, 5, 1),
        "expected": True,
        "gpa": None,          # no GPA yet, so the template skips it
        "coursework": [],
        "honors": [],
    },
    {
        "school": "New York University Tandon School of Engineering",
        "degree": "B.S. in Computer Engineering",
        "location": "New York, USA",
        "start": date(2022, 9, 1),
        "end": date(2026, 5, 1),
        "expected": False,
        "gpa": "3.7/4.0",
        "coursework": [
            "Data Structures & Algorithms",
            "Computer Architecture",
            "Digital Logic and State Machine Design",
            "OOP (C++)",
            "Databases",
            "Embedded System Design",
            "Data Analysis",
            "Parallel Computing",
            "Business Statistics",
        ],
        "honors": ["Cum Laude", "Dean's List", "Honors Scholar", "NYU Founders Day Award"],
    },
]

# Experience and projects share the same shape (title, org, dates, tech, bullets), so one partial template can render both.
EXPERIENCE = [
    {
        "title": "Software Development Intern",
        "org": "MobiCom Corporation LLC",
        "location": "Ulaanbaatar, Mongolia",
        "start": date(2025, 5, 1),
        "end": date(2025, 9, 1),
        "tech": ["Java", "Quarkus", "Jakarta EE", "JAXB", "Maven"],
        "bullets": [
            "Built and integrated RESTful API endpoints with Quarkus to streamline client-server communication for payments.",
            "Refactored existing Jakarta EE backend logic, reducing payment validation errors and improving reliability.",
            "Parsed and processed structured data using JAXB to support XML-based workflows within the payment pipeline.",
            "Collaborated with senior engineers on Maven-based enterprise projects, gaining hands-on experience in scalable back-end architecture.",
        ],
    },
    {
        "title": "Co-Founder & Tech Strategy Specialist",
        "org": "Monadox, EEG-Based Human-Machine Interface",
        "location": "New York, USA",
        "start": date(2025, 2, 1),
        "end": date(2025, 5, 1),
        "tech": ["Python", "ML/DL", "Signal Processing"],
        "bullets": [
            "Implemented a modular ML pipeline for real-time mental state classification using EEG signal data.",
            "Built scalable architecture enabling easy integration of new signal processing techniques and ML/DL models.",
            "Conducted algorithmic research and benchmarking to optimize performance of cognitive and emotional state classifiers.",
            "Contributed to technical strategy and product direction in a niche, emerging neurotechnology market.",
        ],
    },
]

PROJECTS = [
    {
        "title": "OBSIDIAN",
        "org": "Runway Production Management System",
        "location": None,
        "start": date(2026, 2, 1),
        "end": date(2026, 5, 1),
        "tech": ["Node.js", "Express", "MySQL", "EJS", "DigitalOcean", "Render"],
        "bullets": [
            "Prevented duplicate show conflicts with a BEFORE INSERT trigger enforcing unique sequences at the database layer.",
            "Designed a normalized 11-table MySQL schema with enforced referential integrity.",
            "Isolated user privileges by implementing database-level RBAC via SQL GRANT/REVOKE commands.",
            "Shipped a live platform by deploying Node.js/Express on Render with a DigitalOcean MySQL SSL backend.",
        ],
    },
    {
        "title": "Gestura",
        "org": "ASL Gesture-to-Speech Glove (Senior Capstone)",
        "location": None,
        "start": date(2025, 9, 1),
        "end": None,          # None means ongoing, so the template shows "Present"
        "tech": ["Python", "C", "Raspberry Pi", "BLE", "TFLite"],
        "bullets": [
            "Engineering a wearable glove with 5 flex sensors and a 6-DOF IMU to classify ASL gestures via ML on Raspberry Pi.",
            "Transmitting predictions over BLE to a mobile app with TTS output and an editable gesture dictionary.",
            "Trained a TFLite gesture classifier achieving 90%+ accuracy across 34 ASL signs with under 100 ms on-device inference.",
            "Architected modular C firmware separating sensor, ML, and BLE layers to enable gesture vocabulary expansion.",
        ],
    },
    {
        "title": "Bite Theory",
        "org": "Hoya Hacks",
        "location": None,
        "start": date(2026, 2, 1),
        "end": date(2026, 2, 1),
        "tech": ["Flask", "JavaScript", "HTML/CSS", "Firebase"],
        "bullets": [
            "Built an agentic AI app for real-time ingredient detection and personalized food recommendations.",
            "Used Gemini OCR to scan menus and output instant ingredient breakdowns with allergy and restriction warnings.",
            "Integrated Yelp MCP and Open Nutrition MCP to enrich dishes with ingredient and nutrition data.",
            "Stored evolving taste profiles in MongoDB (allergies, preferences, ratings); shipped an MVP in a hybrid hackathon.",
        ],
    },
    {
        "title": "Parkinson's Symptom Detector",
        "org": "EE4144 Embedded Challenge",
        "location": None,
        "start": date(2025, 1, 1),
        "end": date(2025, 5, 1),
        "tech": ["C++", "PlatformIO", "ATmega32u4", "ADXL345"],
        "bullets": [
            "Classified Parkinson's tremor (3-5 Hz) and dyskinesia (5-7 Hz) via an FFT pipeline on an ATmega32u4 at 52 Hz.",
            "Suppressed false positives using 3-window temporal averaging with intensity thresholding for real-time detection.",
            "Hand-soldered an ADXL345 IMU and TFT touchscreen; wrote modular C++ firmware across sensor, FFT, and UI modules.",
            "As part of a 4-person team, delivered a wearable with live intensity visualization and touch navigation on a 320x240 display.",
        ],
    },
    {
        "title": "PaperPulse",
        "org": "Scholarly Insight",
        "location": None,
        "start": date(2025, 2, 1),
        "end": date(2025, 5, 1),
        "tech": ["Flask", "JavaScript", "HTML/CSS", "Firebase"],
        "bullets": [
            "Built a full-stack web app integrating the arXiv API for dynamic academic paper search, retrieval, and filtering.",
            "Developed a Flask backend with REST endpoints for XML parsing and asynchronous JSON response handling.",
            "Developed a responsive UI and dynamic search features using vanilla JavaScript and modern CSS layout.",
            "Integrated Firebase authentication for secure login and a personalized favorite articles feature.",
        ],
    },
]

# A dictionary: category name -> list of skills. The template loops over
# it with {% for category, items in skills.items %}.
SKILLS = {
    "Languages": ["Python", "C/C++", "Java", "JavaScript", "SQL", "Verilog", "HTML", "CSS"],
    "Frameworks": ["Flask", "Quarkus", "Jakarta EE", "Node.js", "Express", "Django"],
    "Tools": ["Git", "Maven", "MATLAB", "PlatformIO", "OpenMP", "MPI", "Raspberry Pi"],
    "Data": ["MySQL", "MongoDB", "Firebase"],
}


def cv_page(request):
    """Render the full CV. The context dict is the only source of content."""
    context = {
        **PERSON,             # unpacks name, phone, email, links into the context
        "education": EDUCATION,
        "experience": EXPERIENCE,
        "projects": PROJECTS,
        "skills": SKILLS,
        "updated": date.today(),
    }
    return render(request, "cv/cv.html", context)


def contact_page(request):
    """A small second page, mainly so {% url %} links between real pages."""
    return render(request, "cv/contact.html", PERSON)
