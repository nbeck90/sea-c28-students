def rot13(to_rot):
    return to_rot.encode('rot_13')


if __name__ == '__main__':
    assert rot13("Things") == "Guvatf"
    assert rot13("Things and Stuff") == "Guvatf naq Fghss"
    assert rot13("I have 42 things?") == "V unir 42 guvatf?"
