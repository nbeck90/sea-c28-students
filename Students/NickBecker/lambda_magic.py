def func_builder(num_size):
    """Create a list of functions such that they add an inputted number to their index"""
    return [lambda inp1, i = inp2: i + inp1 for inp2 in range(num_size)]

q = func_builder(100)

print q[5](5)

if __name__ == "__main__":
    assert isinstance(q[4], type(func_builder))
    assert q[5](5) == 10
    assert q[10](0) == 10
