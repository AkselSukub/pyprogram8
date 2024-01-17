#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def process_tuple(m):
    n = tuple(i * m_i if i % 2 != 0 else m_i / i for i, m_i in enumerate(m, 1))
    return n

tuple_m = (1, 2, 3, 4, 5)
tuple_n = process_tuple(tuple_m)
print(tuple_n)