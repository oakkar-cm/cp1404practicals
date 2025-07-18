"""
programming_language
Estimate: 20 minutes
Actual: 15 minutes
"""

class ProgrammingLanguage:
    """Represents a programming language with typing style, reflection, and year of release."""

    def __init__(self, name='', typing='', reflection=True, year=0):
        """
        Initialize a ProgrammingLanguage instance.

        :param name: str, the name of the language
        :param typing: str, typing style ('Static' or 'Dynamic')
        :param reflection: bool, whether the language supports reflection
        :param year: int, year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """
        Check if the language uses dynamic typing.

        :return: bool, True if typing is 'Dynamic', else False
        """
        return self.typing.title() == "Dynamic"

    def __str__(self):
        """
        Return a string representation of the programming language.

        :return: str
        """
        return f"{self.name}, {self.typing} Typing, Reflection: {self.reflection}, First appeared in {self.year}"


