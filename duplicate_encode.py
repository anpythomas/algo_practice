# My goal is to complete this challenge without using any pre-built python methods as these can potentially decrease
# efficiency, increasing run time. The following code is a daily workout to increase my ability to build efficient
# algorithms. The goal here is not to complete the mission with the fewest lines of code.

# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
# that character appears only once in the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is a duplicate.
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word):
    """Primary Function"""
    # Create string of all lowercase letters and dictionary with each letter as a key
    letter_dict = {}
    lower_case_word = ''
    for ltr in word:
        ltr = convert_to_lower(ltr)
        lower_case_word += ltr
        letter_dict[ltr] = 0


    # Add values to dictionary's
    for key in letter_dict:
        ctr = 0
        for letter in lower_case_word:
            if key == letter:
                ctr += 1
        letter_dict[key] = ctr

    final_string = ""
    for letter in lower_case_word:
        if letter_dict[letter] > 1:
            final_string += ")"
        else:
            final_string += "("
    return final_string


def convert_to_lower(char):
    """Convert char to lowercase"""
    if 65 <= ord(char) <= 90:
        lower_char = ord(char) + 32
        return chr(lower_char)
    else:
        return char


print(duplicate_encode("Tatter"))
