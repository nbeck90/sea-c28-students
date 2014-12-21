def generate_sum(start=1, stop=200, step=1):
    """Generates the sum of all the previous numbers"""
    i = start
    while i < stop:
        yield i
        step = step + i
        i += step


def generate_double():
    """Double the last number yielded"""
    i = 1
    while i < 300:
        yield i
        i = i * 2


def generate_fibb():
    """Generates Fibonacci Sequence numbers until it passes 200"""
    x, y = 0, 1
    while x < 200:
        yield x
        x, y = y, x + y


def generate_prime():
    """Generates prime numbers indefinitely"""
    i = 2
    while True:
        for nums in range(2, i + 1):
                if i == 2:
                    break
                if i == nums:
                    yield i
                elif i % nums == 0:
                    break
        i = i + 1
