import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        try:
            # autosuggest=False to prevent unexpected suggestions
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary[:500] + "...")
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
