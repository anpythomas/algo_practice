# Complete as quick as possible
#
# Completion Time: 4m25s16

# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

sample_list = [1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5]


def find_it(seq):
    my_set = set(seq)
    for item in my_set:
        val = seq.count(item)
        if val % 2 == 1:
            return item


print(find_it(sample_list))
