from __future__ import division


def find_fractions_of_elements(arr, n):
    positive_nums = 0
    negative_nums = 0
    zero_nums = 0

    for num in arr:
        if num == 0:
            zero_nums += 1
        elif num < 0:
            negative_nums += 1
        else:
            positive_nums += 1

    print "{:.6f}".format(positive_nums/n)
    print "{:.6f}".format(negative_nums/n)
    print "{:.6f}".format(zero_nums/n)

find_fractions_of_elements([-4, 3, -9, 0, 4, 1], 6)
