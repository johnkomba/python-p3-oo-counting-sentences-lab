#!/usr/bin/env python3

import io
import sys
import pytest

class MyString:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self._value and self._value.endswith("."):
            return True
        return False

    def is_question(self):
        if self._value and self._value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self._value and self._value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        if not self._value:
            return 0

        separator = "|"
        temp_value = self._value.replace(".", separator).replace("?", separator).replace("!", separator)
        sentences = [sentence for sentence in temp_value.split(separator) if sentence]

        return len(sentences)


def test_is_class():
    string = MyString()
    assert isinstance(string, MyString)

def test_value_string():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    string = MyString()
    string.value = 123
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "The value must be a string.\n"

def test_is_sentence():
    assert MyString("Hello World.").is_sentence() == True
    assert MyString("Hello World").is_sentence() == False

def test_is_question():
    assert MyString("Is anybody there?").is_question() == True
    assert MyString("Is anybody there").is_question() == False

def test_is_exclamation():
    assert MyString("It's me!").is_exclamation() == True
    assert MyString("It's me").is_exclamation() == False

def test_count_sentences():
    simple_string = MyString("one. two. three?")
    empty_string = MyString()
    complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
    assert simple_string.count_sentences() == 3
    assert empty_string.count_sentences() == 0
    assert complex_string.count_sentences() == 4

if __name__ == "__main__":
    pytest.main()
