from multiprocessing import Pool


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        return n


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        my_list = pool.map(is_prime, range(2, 100000))
        print(sum(filter(None, my_list)))
