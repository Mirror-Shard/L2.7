#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Множество гласных
    vocales = {'a', 'e', 'u', 'i', 'o', 'у', "у", "е", "ы", "а", "о", "э", "я", "и", "ю"}

    # Количество гласных в строке
    vocales_in_linea = 0

    # Ввод строки
    linea = input("Введите строку символов: ").lower()

    # Проходит по всем гласным
    for vocal in vocales:
        # И проверяет их наличие в строке
        if vocal in linea:
            vocales_in_linea += 1

    print(f"Гласных в строке: {vocales_in_linea}")
