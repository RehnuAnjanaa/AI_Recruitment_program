import json

skills = [
    "AI",
    "Machine Learning",
    "Deep Learning",
    "Data Analysis",
    "Data Science"
]

technologies = [
    "CNN",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Django",
    "Flask"
]

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "SQL"
]

resume_text = """
I am a Computer Science student with experience in Python and Java.

I have worked on Machine Learning and Deep Learning projects.

I built CNN models using TensorFlow and PyTorch.

I also have experience with Pandas, NumPy and SQL for Data Analysis.
"""

found_skills = []
found_technologies = []
found_languages = []

for skill in skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

for technology in technologies:
    if technology.lower() in resume_text.lower():
        found_technologies.append(technology)

for language in languages:
    if language.lower() in resume_text.lower():
        found_languages.append(language)

result = {
    "skills": found_skills,
    "technologies": found_technologies,
    "languages": found_languages
}

print(json.dumps(result, indent=4))

job_roles = {
    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "PyTorch"
    ],
    "Data Analyst": [
        "Python",
        "SQL",
        "Pandas",
        "Data Analysis"
    ],
    "Python Developer": [
        "Python",
        "Django",
        "Flask"
    ],
    "AI Engineer": [
        "Python",
        "AI",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow"
    ]
}

candidate_skills = (
        found_skills +
        found_technologies +
        found_languages
)

role_scores = {}

for role, requirements in job_roles.items():

    matched = 0

    for requirement in requirements:
        if requirement.lower() in [skill.lower() for skill in candidate_skills]:
            matched += 1

    score = (matched / len(requirements)) * 100

    role_scores[role] = score

print("\n===== JOB ROLE SUGGESTIONS =====")

sorted_roles = sorted(
    role_scores.items(),
    key=lambda item: item[1],
    reverse=True
)

for role, score in sorted_roles:
    print(f"{role}: {score:.2f}% match")