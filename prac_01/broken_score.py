"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



score = float(input("Enter score: "))
if score < 0:
    print("Invalid Score!")
elif score > 100:
    print("Invalid Score!")
elif score >= 90:
    print("Excellent!")
elif score >= 50:
    print("Pass!")
else:
    print("Bad!")