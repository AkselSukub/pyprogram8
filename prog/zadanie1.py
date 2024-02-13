#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def transform_tuple(t):
    result = ()
    for i, m in enumerate(t):
        if i % 2 != 0:
            n = i * m
        else:
            n = m / i
        result += (n,)
    return result

if __name__ == '__main__':
    # Пример использования
    my_tuple = (1, 2, 3, 4, 5)
    transformed_tuple = transform_tuple(my_tuple)
    print(transformed_tuple)