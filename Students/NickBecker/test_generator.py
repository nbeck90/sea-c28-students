import pytest
import generator


def test_sum():
    it = generator.generate_sum()
    for i in it:
        return i
    assert it.next() == 1
    assert it.next() == 3
    assert it.next() == 6
    assert it.next() == 10
    assert it.next() == 15


def test_double():
    d = generator.generate_double()
    for i in d:
        return i
    assert d.next() == 1
    assert d.next() == 2
    assert d.next() == 4
    assert d.next() == 8
    assert d.next() == 16
    assert d.next() == 32


def test_fibb():
    fi = generator.generate_fibb()
    for i in fi:
        return i
    assert fi.next() == 0
    assert fi.next() == 1
    assert fi.next() == 1
    assert fi.next() == 2
    assert fi.next() == 3
    assert fi.next() == 5


def test_prime():
    p = generator.generate_prime()
    for i in p:
        return i
    assert p.next() == 3
    assert p.next() == 5
    assert p.next() == 7
    assert p.next() == 11
    assert p.next() == 13
    assert p.next() == 17
