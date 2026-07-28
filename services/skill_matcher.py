import re


SKILLS = [

    "python",
    "java",
    "sql",
    "aws",
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "linux",
    "react",
    "spring boot",
    "mongodb",
    "mysql",
    "postgresql",
    "terraform",
    "airflow",
    "spark",
    "hadoop"
]


def find_missing_skills(resume_text, jd_text):

    resume = resume_text.lower()

    jd = jd_text.lower()

    jd_skills = []

    resume_skills = []

    for skill in SKILLS:

        if skill in jd:
            jd_skills.append(skill)

        if skill in resume:
            resume_skills.append(skill)

    missing = list(
        set(jd_skills) - set(resume_skills)
    )

    matched = list(
        set(jd_skills) & set(resume_skills)
    )

    return matched, missing