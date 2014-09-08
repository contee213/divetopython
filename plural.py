# -*- coding: utf-8 -*-

__author__ = 'contee'

"""
plural
~~~~~~~~~~~~~~

file commment here.

"""

import re

def build_match_and_apply_function(pattern, search, replace):
    def match(word):
        return re.search(pattern, word)
    def apply(word):
        return re.sub(search, replace, word)
    return match, apply

class LazyRule:
    """

    """
    file_name = "plural.txt"

    def __init__(self):
        self.pattern_file= open(self.file_name, mode='r', encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):

        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        print("--- readline {0} ---".format(self.cache_index))
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(sep=None, maxsplit=3)
        func = build_match_and_apply_function(pattern, search, replace)
        self.cache.append(func)
        return func

rules = LazyRule()

test_pattern = [
    'caps', 'mark', 'rock',
    'vacancy', 'agency', 'boy', 'day', 'pita',
    'dish', 'hash', 'yeah'
]

for word in test_pattern:
    for match, apply in rules:
        if match(word):
            print(apply(word))
            break