from fractions import Fraction
from sys import argv
import os.path

__INNER__PARAMS = argv[1:]


def read_circle(path):
    with open(path, 'r', encoding='utf-8') as file:
        coord, radius = (file.readline().strip() for _ in range(2))
        return coord, radius


def read_dots(path):
    with open(path, 'r', encoding='utf-8') as file:
        dot_list = [row.strip() for row in file.readlines()]
        return dot_list


def dot_check(c_x, c_y, c_radius, d_x, d_y):
    segment = ((d_x - c_x) ** 2 + (d_y - c_y) ** 2) ** 0.5
    return 0 if segment == c_radius else 2 if segment > c_radius else 1


def print_dots_check(path_circle, path_dots):
    c_coord, c_radius = read_circle(path_circle)
    dot_list = read_dots(path_dots)

    for row in dot_list:
        try:
            c_x, c_y = (Fraction(i) for i in c_coord.split())
            radius = Fraction(c_radius)
            d_x, d_y = (Fraction(j) for j in row.split())
            print(dot_check(c_x=c_x, c_y=c_y, c_radius=radius, d_x=d_x, d_y=d_y))

        except ValueError as e:
            print(e)


if __name__ == '__main__':
    if len(__INNER__PARAMS) != 2:
        print('Программа должна принять два аргумента (пути к файлам с координатами)')
    else:
        if not os.path.exists(__INNER__PARAMS[0]) or not os.path.exists(__INNER__PARAMS[1]):
            print('Файлы с координатами не найдены')
        else:
            print_dots_check(path_circle=__INNER__PARAMS[0], path_dots=__INNER__PARAMS[1])
