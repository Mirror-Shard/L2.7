#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Ввод двух строк
    linea1 = set(input("Введите первую строку символов: "))
    linea2 = set(input("Введите вторую строку символов: "))

    # Вывод общих символов для двух строк
    print(f"Общие символы для строк: {linea1.intersection(linea2)}")
