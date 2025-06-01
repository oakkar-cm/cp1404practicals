def main():
    score = get_valid_score()

    menu = """\nMenu:
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""

    choice = choice_menu(menu)

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")

        choice = choice_menu(menu)

    print("Farewell!")

def choice_menu(menu):
    print(menu)
    choice = input("Enter your choice: ").strip().upper()
    return choice

def get_valid_score():
    score = float(input("Enter your score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = float(input("Enter your score (0–100): "))
    return score

def determine_result(score):
    if score >= 90:
        return "Excellent!"
    elif score >= 50:
        return "Passable!"
    else:
        return "Bad!"

def print_stars(score):
    print("*" * int(score))

main()