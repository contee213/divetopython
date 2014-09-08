# -*- coding: utf-8 -*-

__author__ = 'contee'

"""
byende
~~~~~~~~~~~~~~

file commment here.

"""

s = 'あいうえお'
b = s.encode('utf-8')
f = b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'
print(b)
print(f.decode('utf-8'))