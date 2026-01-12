import pandas as pd
from collections import Counter

print("Loading cleaned data...")

df = pd.read_csv("../data/cleaned_jobs.csv")

# Skill list (can grow later)
skill_list = [
    "python", "sql", "excel", "power bi", "tableau",
    "machine learning", "deep learning", "nlp",
    "aws", "azure", "docker", "spark", "pandas"
]

all_skills = []

print("Extracting skills...")

for _, row in df.iterrows():
    text = ""

    if "job_description" in df.columns:
        text += str(row.get("job_description", ""))
    if "skills" in df.columns:
        text += " " + str(row.get("skills", ""))

    text = text.lower()

    for skill in skill_list:
        if skill in text:
            all_skills.append(skill)

skill_counts = Counter(all_skills)

skills_df = pd.DataFrame(skill_counts.items(), columns=["skill", "demand_count"])
skills_df = skills_df.sort_values(by="demand_count", ascending=False)

skills_df.to_csv("../data/skill_demand.csv", index=False)

print("skill_demand.csv created!")
print(skills_df.head(10))
