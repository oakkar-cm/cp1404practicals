"""
Project class for project management.
Estimated time: 3 hours.
"""

from datetime import datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __lt__(self, other):
        """Sort by priority (then date if priorities are equal)."""
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.start_date < other.start_date

    def is_complete(self):
        """Return True if the project is complete (100% done)."""
        return self.percent_complete >= 100

    @staticmethod
    def from_tab_line(line):
        """Create a Project from a tab-separated string (excluding header)."""
        parts = line.strip().split('\t')
        # Name	Start Date	Priority	Cost Estimate	Completion Percentage
        name = parts[0]
        start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        percent_complete = int(parts[4])
        return Project(name, start_date, priority, cost_estimate, percent_complete)

    def to_tab_line(self):
        """Convert the Project to a tab-separated string suitable for saving."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.percent_complete}"

    def __str__(self):
        """String representation for user display."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%")