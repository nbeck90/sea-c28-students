def fibonacci(n):
    """Return the nth number of the Fibonacci series"""
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth number of the Lucas series"""
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(x, y=0, z=1):
    """
    Return the xth value of a chosen series

    """
    if y == 0 and z == 1:
        return fibonacci(x)
    elif y == 2 and z == 1:
        return lucas(x)
    else:
        return sum_series(x - 1, y, z) + sum_series(x - 2, y, z)

print lucas(12)

if __name__ == '__main__':
    assert fibonacci(15) == 610 #ensuring the fibonacci sequence functions
    assert fibonacci(1) and fibonacci(2) == 1 #determining both 1 and 2 in fibonacci will both return 1
    assert lucas(0) == None #Lucas should start at 2 when 1 is called, and None otherwise
    assert lucas(1) == 2 #first of the Lucas series
    assert lucas(12) == 199 #going far away from 1, just determining a random point is correct
    assert sum_series(1, 0, 1) == 1   #sum_series dictates that item 1 of the Fibonacci series is 1
    assert sum_series(6, 2, 1) == 11  #sum_series dictates that item 6 of the Lucas series is 11
    assert sum_series(10, 0, 1) == 55   #sum_series dictates that item 10 in the Fibonacci series is 55
    print "functions working properly"
