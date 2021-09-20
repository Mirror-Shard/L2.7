#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Универсальное множество всех букв
    all = set("abcdefghijklmnopqrstuvwxyz")

    # Переменные из учебника
    a = {'c', 'g', 'h', 'i', 'j'}
    b = {'c', 'd', 'i', 'o', 's'}
    c = {'i', 'j', 'r', 'z'}
    d = {'b', 'c', 'f', 'i', 'w', 'x'}

    # Операции из учебника
    x = (a.union(b)).intersection(d)
    y = (a.difference(d)).union((all - c).difference(all - b))

    # Вывод результатов
    print(x)
    print(y)
