import pytest
import ROT13


def test_basic_shift():
    assert ROT13.rot13("things") == "guvatf"


def test_Upper_lower():
    assert ROT13.rot13("Things and Stuff") == "Guvatf naq Fghss"


def test_number_letters():
    assert ROT13.rot13("I have 42 things?") == "V unir 42 guvatf?"
