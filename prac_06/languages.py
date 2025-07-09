from programming_language import ProgrammingLanguage

def main():
    # Create language instances
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print one language as example
    print(python)
    print()

    # Store all languages in a list
    languages_list = [python, ruby, visual_basic]

    # Filter only dynamically typed languages
    dynamic_languages = [lang for lang in languages_list if lang.is_dynamic()]

    print('The dynamically typed languages are:')
    for lang in dynamic_languages:
        print(lang.name)

if __name__ == '__main__':
    main()
"prac06"