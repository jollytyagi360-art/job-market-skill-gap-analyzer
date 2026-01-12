import pandas as pd

print("Loading dataset...")

df = pd.read_csv("../data/job_descriptions.csv")

print("Total rows:", len(df))
print("Columns found:")
print(df.columns)

# Select required columns safely
col_map = {
    "Job Title": "job_title",
    "Company": "company",
    "location": "location",
    "Job Description": "job_description",
    "skills": "skills"
}

available_cols = [c for c in col_map.keys() if c in df.columns]

df = df[available_cols]

# Rename columns
df = df.rename(columns=col_map)

# Basic cleaning
df = df.dropna(subset=["job_title"])
df = df.drop_duplicates()

# Convert text to lowercase
for col in df.columns:
    df[col] = df[col].astype(str).str.lower().str.strip()

# Save cleaned file
df.to_csv("../data/cleaned_jobs.csv", index=False)

print("cleaned_jobs.csv created successfully!")
print("Final shape:", df.shape)
