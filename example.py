from my_functions import dist, dist_complex


if __name__ == '__main__':
    print('File \'main.py\' is running as process 0')
    print(dist.get_dist(1, 1, 5, 5))
    print(dist_complex.get_dist_square(1, 1, 5, 5))
