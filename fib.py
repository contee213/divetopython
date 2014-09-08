# -*- coding: utf-8 -*-

__author__ = 'contee'

"""
fib
~~~~~~~~~~~~~~

file commment here.

"""

class Fib:
    """
    """

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        f = self.a
        if f > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return f

f = Fib(100)

for x in f:
    print(x)