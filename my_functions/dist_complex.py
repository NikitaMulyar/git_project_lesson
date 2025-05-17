from math import sqrt


def get_dist_square(x1, y1, x2, y2):
    """Квадрат расстояния между точками"""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2


if __name__ == '__main__':
    print('File \'dist_complex.py\' is running as process 0')
