# Classify a person's age group : <13 child, 13-19 - Teenager, 20-59 - Adult, 60+ - Senior

age = int (input("Provide me a age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 59:
    print("Adult")
else:
    print("Senior")