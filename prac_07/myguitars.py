from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    guitars += get_new_guitars()

    print("\nSorted guitars:")
    guitars.sort()
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, year, cost = parts
                    guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars

def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def get_new_guitars():
    """Prompt the user to add new guitars."""
    new_guitars = []
    print("\nEnter your new guitars. Leave name blank to finish.")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return new_guitars

def save_guitars(filename, guitars):
    """Write all guitars to a CSV file."""
    with open(filename, "w", encoding="utf-8") as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)

if __name__ == "__main__":
    main()