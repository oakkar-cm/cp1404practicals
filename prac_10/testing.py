"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car_default = Car()
    assert car_default.fuel == 0, "Car does not set default fuel correctly"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel correctly when specified"


def format_phrase_as_sentence(phrase):
    """
    Format phrase as sentence, capitalized and ending with a single full stop.

    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('goodbye!')
    'Goodbye!'
    """
    phrase = phrase.strip()
    if not phrase.endswith(('.', '!', '?')):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]


run_tests()
doctest.testmod()