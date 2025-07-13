class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):  # ADDED pointer_arithmetic parameter
        """Construct a ProgrammingLanguage from the given values.

        :param name: str - Name of the language
        :param typing: str - Typing discipline
        :param reflection: bool - Supports reflection
        :param year: int - Year first appeared
        :param pointer_arithmetic: bool - Supports pointer arithmetic   # ADDED docstring for new field
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic  # ADDED new attribute

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}")  # MODIFIED to include new field

    def __str__(self):
        """Return a user-friendly string representation."""
        return self.__repr__()  # ADDED __str__ to match __repr__

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)  # UPDATED
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)  # UPDATED
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)  # UPDATED
    c_lang = ProgrammingLanguage("C", "Static", False, 1972, True)  # NEW example with pointer arithmetic

    languages = [ruby, python, visual_basic, c_lang]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)