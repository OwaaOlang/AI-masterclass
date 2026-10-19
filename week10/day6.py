# Build a simple project pricing calculator
def calculate_price(hours, rate=25, complexity=1.0):
    base = hours * rate
    return base * complexity

print(f"Simple script (5h): ${calculate_price(5):.0f}")
print(f"Medium project (15h): ${calculate_price(15, complexity=1.2):.0f}")
print(f"Complex project (30h): ${calculate_price(30, complexity=1.5):.0f}")

# Write a structured service offer in Python
service = {
    "title": "AI Automation Scripts for Small Businesses",
    "problem": "Manual data entry and report generation waste hours every week.",
    "solution": "I build Python scripts that automate your data workflows.",
    "deliverable": "A working script, tested, documented, and handed over.",
    "price": "Starting from $150 per project"
}
for key, val in service.items():
    print(f"{key.upper()}: {val}")

    # Build a simple project pricing calculator
def calculate_price(hours, rate=25, complexity=1.0):
    base = hours * rate
    return base * complexity

print(f"Simple script (5h): ${calculate_price(5):.0f}")
print(f"Medium project (15h): ${calculate_price(15, complexity=1.2):.0f}")
print(f"Complex project (30h): ${calculate_price(30, complexity=1.5):.0f}")

# Generate a client proposal template
client = "James"
project = "Automated Monthly Sales Report"
timeline = "7 days"
price = 200

print(f"Hi {client},")
print(f"\nThank you for your interest. Here is my proposal for the {project}.")
print(f"\nDeliverable: A Python script that generates your monthly report automatically.")
print(f"Timeline: {timeline}")
print(f"Investment: ${price}")
print("\nLet me know if you have questions.")

# Print a structured 12-month growth plan
plan = [
    ("Months 1-2", "Land first 2 paid clients using existing portfolio"),
    ("Months 3-4", "Build one SaaS micro-tool and launch it"),
    ("Months 5-6", "Raise rates and specialize in one niche"),
    ("Months 7-9", "Scale to 3-5 recurring clients"),
    ("Months 10-12", "Hit monthly income target and document the process")
]
print("12-Month Growth Plan")
print("-" * 40)
for period, goal in plan:
    print(f"{period}: {goal}")

    def service_offer(skill, price, delivery):
        return f"Service: [skill] | Price: KES [price] | Delivery: [delivery] days"