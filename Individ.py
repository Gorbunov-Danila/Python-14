#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_area(type=0):
    """
    Возвращает функцию для вычисления площади фигуры.
    По умолчанию type = 0, что соответствует треугольнику.
    """
    def triangle_area(base, height):
        return 0.5 * base * height

    def rectangle_area(length, width):
        return length * width

    if type == 0:
        return triangle_area
    else:
        return rectangle_area


# Пример использования
if __name__ == "__main__":
    # Создаем функцию для вычисления площади треугольника
    triangle_calculator = calculate_area(0)

    # Вызываем внутреннюю функцию с параметрами треугольника
    triangle_result = triangle_calculator(5, 8)
    print(f"Площадь треугольника: {triangle_result}")

    # Создаем функцию для вычисления площади прямоугольника
    rectangle_calculator = calculate_area(1)

    # Вызываем внутреннюю функцию с параметрами прямоугольника
    rectangle_result = rectangle_calculator(4, 6)
    print(f"Площадь прямоугольника: {rectangle_result}")
