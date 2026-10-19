
# Git is a terminal tool, not Python.
# Use this terminal to review the logic behind each command.

# Simulate tracking changes
changes = []
changes.append("Created hello.py")
changes.append("Added user input")
changes.append("Fixed loop bug")

for i, msg in enumerate(changes, 1):
    print(f"commit {i}: {msg}")


    # Simulate a branching workflow in Python
branches = {"main": ["initial commit", "add README"],
             "feature": ["add login page", "check login bug"]
             }

current = "main"
print(f"On branch: {current}")
for commit in branches[current]:
    print(f"  {commit}")

#switch branch like git checkout

print("\nSwitching branch")
current ="feature"
print(f"On branch: {current}")
for commit in branches [current]:
    print(f" {commit}")



# Simulate merging a feature branch into main
branches = {
    "main": ["initial commit", "add README"],
    "feature": ["add login page", "add auth logic"]
}

# Merge feature into main
branches["main"].extend(branches["feature"])
print("After merge, main branch history:")
for commit in branches["main"]:
    print(f"  {commit}")


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