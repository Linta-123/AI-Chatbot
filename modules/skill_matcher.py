import json

def match_skills(resume_text, role):
    with open("data/role_skills.json", "r") as file:
        role_data = json.load(file)

    expected_skills = role_data.get(role, [])
    found = []
    missing = []

    resume_lower = resume_text.lower()

    for skill in expected_skills:
        if skill.lower() in resume_lower:
            found.append(skill)
        else:
            missing.append(skill)

    return found, missing