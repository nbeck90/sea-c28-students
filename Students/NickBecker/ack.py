def A(m, n):
    """Return the Ackermann Function of two integers n and m"""
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n-1))

if __name__ == '__main__':
    assert A(1, 1) == 3
    assert A(2, 1) == 5
    assert A(3, 1) == 13
    assert A(1, 0) == 2
    assert A(2, 0) == 3
    assert A(3, 0) == 5
    assert A(1, 2) == 4
    assert A(2, 2) == 7
    assert A(3, 2) == 29
    assert A(0, 1) == 2
    assert A(0, 2) == 3
    assert A(0, 3) == 4
    assert A(0, 0) == 1
    assert A(1, 3) == 5
    assert A(2, 3) == 9
    assert A(3, 3) == 61
    print "All Tests Pass"
