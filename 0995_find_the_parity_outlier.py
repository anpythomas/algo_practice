# Complete as quick as possible
#
# Completion Time: 21m35s90
#
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The
# array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer
# N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

text_string = [3, 4, 5, 7]

def find_outlier(integers):
    my_dict = {}
    ctr_odd = 0
    ctr_even = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 1:
            ctr_odd += 1
            my_dict[integers[i]] = "odd"
        elif integers[i] % 2 == 0:
            ctr_even += 1
            my_dict[integers[i]] = "even"
    if ctr_even > 1:
        for num in my_dict:
            if my_dict[num] == "odd":
                return num
    else:
        for num in my_dict:
            if my_dict[num] == "even":
                return num


print(find_outlier(text_string))