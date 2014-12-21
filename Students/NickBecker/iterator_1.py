#!/usr/bin/env python


class IterateMe_1(object):

    def __init__(self, start=1, stop=11, step=1):
        self.start = start
        self.step = step
        self.current = self.start - self.step
        self.stop = stop

    def __iter__(self):
        self.current = self.start - self.step
        return self

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print "first version"
    for i in IterateMe_1():
        print i
