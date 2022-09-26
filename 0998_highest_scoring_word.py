# Complete as quick as possible.
#
# Completion Time: 22m17s82
#
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

ex_string = 'man i need a taxi up to ubud'

def high(x):
    # Create list with each word as a separate string
    string_list = ex_string.split()

    # Create default values for dict
    default_key = "none"
    highest_word = {default_key: 0}

    # Iterate through words
    for word in string_list:
        ctr = 0

        # Iterate through each letter of each word, convert to it's value and add to the total variable titled "ctr"
        for letter in word:
            char_value = convert_char_to_points(letter)
            ctr += char_value

        # If the total word score is higher than the highest word variable in the dictionary, add new word to dict and
        # remove previous high word
        if ctr > highest_word[default_key]:
            del highest_word[default_key]
            highest_word[word] = ctr
            default_key = word

    return default_key


def convert_char_to_points(char):
    """Convert char to it's point value"""
    return (ord(char) - 96)


print(high(ex_string))

# Completion Time: 22m17s82
