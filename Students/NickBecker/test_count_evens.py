#!/usr/bin/env python

import pytest
import count_evens


def test_count_evens():
    assert count_evens.count_evens([2, 4, 5, 1, 0]) == 3


def test_count_repeats():
    assert count_evens.count_evens([2, 2, 2, 4, 4, 5]) == 5


def test_empty():
    assert count_evens.count_evens([]) == 0


def test_count_error():
    with pytest.raises(TypeError):
        assert count_evens.count_evens(["String"])
