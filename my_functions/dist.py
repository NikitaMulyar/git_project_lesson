from math import sqrt


def get_dist(x1, y1, x2, y2):
    """Расстояние между точками на Декартовой плоскости"""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    print('File \'dist.py\' is running as process 0')
    print(get_dist.__doc__)
