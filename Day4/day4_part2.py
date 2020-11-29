import sys

l_to_int = lambda l: list(map(lambda s: int(s), l))
l_to_str = lambda l: list(map(lambda s: str(s), l))


def get_first_suitable_n(low):
    n_as_l = l_to_int(list(str(low)))
    min_n = None
    has_dup = False
    for i in range(len(n_as_l)):
        if min_n is None or n_as_l[i] > min_n:
            min_n = n_as_l[i]
        elif n_as_l[i] < min_n:
            n_as_l[i] = min_n
        if i > 0:
            if n_as_l[i] == n_as_l[i - 1]:
                has_dup = True
    if not has_dup:
        n_as_l[-2] = n_as_l[-1]
    return int(''.join(l_to_str(n_as_l)))


def generate(low, high):
    while True:
        low = get_first_suitable_n(low)
        if low < high:
            yield low
        else:
            return
        low += 1


if __name__ == '__main__':
    lower, upper = 146810, 612564
    # lower, upper = int(sys.argv[1]), int(sys.argv[2])
    ns = list(generate(lower, upper))

    print(len(ns))
