def func_builder(num_size):
    """Create a list of functions such that they add an inputted number to their index"""
    return [lambda inp1, i = inp2: i + inp1 for inp2 in range(num_size)]

print func_builder(90)

if __name__ == "__main__":
    #FIX THIS AS WELL AS THE INPUTS
