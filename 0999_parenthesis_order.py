# Goal: Complete Mission

# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
# function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
#
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

my_string = "(())()()(())"

def paren(my_string):
    ctr = 0
    for char in my_string:
        if char == "(":
            ctr += 1
        elif char == ")":
            ctr -= 1
            if ctr < 0:
                return False
    if ctr == 0:
        return True
    else:
        return False


print(paren(my_string))