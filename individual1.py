#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import test1  # Импортируем наш модуль

if __name__ == '__main__':
    # Пример использования замыкания
    my_list = ["строка_1", "строка_2", "строка_3"]
    html_list_generator = test1.create_html_list(my_list)  # Используем функцию из модуля
    result_html = html_list_generator()

    print(result_html)
