# -*- coding: utf-8 -*-

__author__ = 'contee'

"""
multilize
~~~~~~~~~~~~~~

file comment here.

"""

import re

def multilize_english(s):

    if re.search('[sxz]$', s):
        return re.sub('$', 'es', s)

    elif re.search('[^aeioudgkprt]h$', s):
        return re.sub('$', 'es', s)

    elif re.search('[^aeiou]y$', s):
        return re.sub('y$', 'ies', s)

    else:
        return s + 's'

patterns = (
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('[^aeiou]y$', 'y$', 'ies'),
    ('$', '$', 's')
)

def mls(pattern, remove, replace):
    def match(word):
        return re.search(pattern, word)
    def apply(word):
        return re.sub(remove, replace, word)
    return (match, apply)

rules = [ mls(pattern, remove, replace)
          for (pattern, remove, replace) in patterns]

def nls(noun):
    for (match, apply) in rules:
        if match(noun):
            return apply(noun)

def gmls(pattern, remove, replace):
    yield mls(pattern, remove, replace)

def build_match_and_apply_function(pattern, search, replace):
    def match(word):
        return re.search(pattern, word)
    def apply(word):
        return re.sub(search, replace, word)
    return match, apply

def gen_rules(rule_filename):
    with open(rule_filename, mode='r', encoding='utf-8') as pattern_file:
        for line in pattern_file:
            (pattern, search, replace) = line.split(None, 3)
            yield build_match_and_apply_function(pattern, search, replace)

def plural(noun, rule_filename='plural.txt'):
    for match, apply in gen_rules(rule_filename):
        if match(noun):
            return apply(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

test_pattern = [
    'mark', 'rock', 'caps',
    'vacancy', 'agency', 'boy', 'day', 'pita',
    'dish', 'hash', 'yeah'
]

for test in test_pattern:
    print(multilize_english(test))
    print(nls(test))
    print(plural(test))