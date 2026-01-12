import pandas as pd

# Load skill demand
skills_df = pd.read_csv("../data/skill_demand.csv")

# Load cleaned jobs
jobs_df = pd.read_csv("../data/cleaned_jobs.csv")

total_jobs = len(jobs_df)

print("Total jobs:", total_jobs)

# Calculate gap score
skills_df["gap_score"] = skills_df["demand_count"] / total_jobs

# Sort by gap score
skills_df = skills_df.sort_values(by="gap_score", ascending=False)

# Save result
skills_df.to_csv("../data/skill_gap_analysis.csv", index=False)

print("skill_gap_analysis.csv created!")

print(skills_df.head(10))
