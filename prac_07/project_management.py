"""
Project Management Program.
Estimated time: 3 hours.
"""

from project import Project
from datetime import datetime

DEFAULT_FILENAME = "projects.txt"

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            in_file.readline()  # skip header
            for line in in_file:
                if line.strip():
                    projects.append(Project.from_tab_line(line))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(project.to_tab_line(), file=out_file)

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()
    complete.sort()
    print("Incomplete projects: ")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects: ")
    for p in complete:
        print(f"  {p}")

def filter_projects_by_date(projects):
    """Display projects that start after a given date, sorted by date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_new_project(projects):
    """Prompt user for new project details and add to list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    try:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format, project not added.")
        return
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))

def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    print(project)
    percent_complete_str = input("New Percentage: ")
    priority_str = input("New Priority: ")
    if percent_complete_str:
        project.percent_complete = int(percent_complete_str)
    if priority_str:
        project.priority = int(priority_str)

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")
    choice = ""
    while choice != "Q":
        print(menu)
        choice = input(">>> ").strip().upper()
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
            if save in ("yes", "y"):
                save_projects(DEFAULT_FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()