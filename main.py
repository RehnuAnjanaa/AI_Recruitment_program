import json

text = input("Tell me about your experience or skills: ")

skills = ["AI", "Machine Learning", "Deep Learning"]
technologies = ["CNN", "TensorFlow", "PyTorch"]
languages = ["Python", "Java", "C++"]


found_skills = []
found_technologies = []
found_languages = []


for skill in skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)

for technology in technologies:
    if technology.lower() in text.lower():
        found_technologies.append(technology)

for language in languages:
    if language.lower() in text.lower():
        found_languages.append(language)

result = {
    "skills": found_skills,
    "technologies": found_technologies,
    "languages": found_languages
}

print(json.dumps(result, indent=4))