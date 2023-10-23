# You are given a string containing a series of words separated by spaces.
# Write a function to reverse the order of the words in the string.
# For example, given the input string "Hello World OpenAI",
# your function should return "OpenAI World Hello".

def reverseWords(str):
    splt_str = str.split(' ')
    res = " ".join(reversed(splt_str))
    return res



print(reverseWords("Hello world"))