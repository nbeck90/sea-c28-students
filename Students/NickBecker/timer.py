import time


class Timer(object):
    """Prints time elapsed from file start to file finish"""
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self.start

    def __exit__(self, *args):
        self.finished = time.time()
        self.elapsed = self.finished - self.start
        print "Code took {} seconds to finish".format(self.elapsed)
        return self
