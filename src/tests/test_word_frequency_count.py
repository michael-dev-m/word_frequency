import pytest
from collections import Counter
from src.wf_count.word_frequency_count import count_words

data_text = [
    ("Hello! My name is John", {"hello": 1, "my": 1, "name": 1, "is": 1, "john": 1,}),
    ("(Hello! Hello)", {"hello": 2}),
    ("Hi. How are you? ", {"hi": 1, "how": 1, "you": 1, "are": 1}),
    ("It's good", {"good": 1}),
    ("stand-alone", {"stand-alone": 1}),
    (";", {}),
    ("I", {}),
    ("", {}),
    ("count_animals == 5", {}),
    (" len(new_zoo)-1+len(new_zoo[2]) 1", {}),
    ("count7 ", {"count": 1}),
    ("_variable", {}),
    ("first.py", {}),
    ("nameClass", {})
]
@pytest.mark.parametrize("text, expected", data_text)
def test_count_words(text, expected):
    assert count_words(text) == Counter(expected)
