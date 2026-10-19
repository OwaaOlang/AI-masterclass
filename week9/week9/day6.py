

 # Write a Python script that generates a README template
# for a GitHub project
project = "AI Text Summariser"
desc = "A Python tool that summarises long text using the OpenAI API."
tech = ["Python", "OpenAI API", "Flask"]

print(f"# {project}")
print(f"\n{desc}\n")
print("## Tech Stack")
for t in tech:
    print(f"- {t}")

#A carpenter has been version-controlling his pricing calculator script. Print the full commit history,
#  numbered, with the date and message. This mirrors exactly what git log shows on a project
    
    commits = [
    {"hash": "a1b2c3", "date": "2026-06-01", "message": "Initial commit: basic chair price calculator"},
    {"hash": "d4e5f6", "date": "2026-06-03", "message": "Add timber cost per metre calculation"},
    {"hash": "g7h8i9", "date": "2026-06-05", "message": "Fix rounding error in total material cost"},
    {"hash": "j0k1l2", "date": "2026-06-08", "message": "Add labour cost per day input"},
    {"hash": "m3n4o5", "date": "2026-06-10", "message": "Add profit margin calculator"},
]

print("Commit History: Carpentry Pricing Tool")
print("-" * 50)
for i, c in enumerate(commits, 1):
    print(f"{i}. [{c['hash']}] {c['date']}: {c['message']}")

print(f"\nTotal commits: {len(commits)}")
print(f"Latest: {commits[-1]['message']}")

#Excercise 1

commit = [
     "Initial commit"
     "Add SMP tracker script"
     "Fix loop logic in day5.py"
     "Add requirements.txt"
]

for i, message in enumerate(commits, 1):
    print(f" {i} . {message}")