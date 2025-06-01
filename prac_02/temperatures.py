menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(menu)
choice = input(">>> ").upper()

def celsius_to_fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def fahrenheit_to_celsius():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celsius_to_fahrenheit()
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        fahrenheit_to_celsius()
    else:
        print("Invalid option")
    print(menu)
    choice = input(">>> ").upper()
print("Thank you.")