import numpy as np
from time import time


def levenshtein1(source, target):
    if len(source) < len(target):
        return levenshtein1(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]


def levenshtein2(source, target):
    ''' From Wikipedia article; Iterative with two matrix rows.'''
    if source == target:
        return 0
    elif len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)

    v0 = [None] * (len(target) + 1)
    v1 = [None] * (len(target) + 1)

    for i in range(len(v0)):
        v0[i] = i

    for i in range(len(source)):
        v1[0] = i + 1

        for j in range(len(target)):
            cost = 0 if source[i] == target[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)

        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(target)]


def main():
    start_time = time()
    [levenshtein1('kitten', 'mathematics') for i in range(10000)]
    end_time = time()
    print('found {0} in {1} seconds'.format(levenshtein1('philosophy', 'mathematics'), end_time - start_time))

    start_time = time()
    [levenshtein1('kitten', 'mathematics') for i in range(10000)]
    end_time = time()
    print('found {0} in {1} seconds'.format(levenshtein2('philosophy', 'mathematics'), end_time - start_time))


if __name__ == '__main__':
    main()
