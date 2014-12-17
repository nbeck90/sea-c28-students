import ack
import pytest


def test_ack():

    ack_combos = [

                  (1, 1, 3),
                  (2, 1, 5),
                  (3, 1, 13),
                  (2, 0, 3),
                  (3, 0, 5),
                  (1, 2, 4),
                  (2, 2, 7),
                  (3, 2, 29),
                  (0, 1, 2),
                  (0, 2, 3),
                  (0, 3, 4),
                  (0, 0, 1),
                  (1, 3, 5),
                  (2, 3, 9),
                  (3, 3, 61)

                 ]

    for inp1, inp2, result in ack_combos:
        assert ack.A(inp1, inp2) == result
