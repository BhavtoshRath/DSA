# Sol 1: Brute force


# How is below approach time O(N^2): according to algoExpert?
def isPalindrome1(string):
    rev_string = ""
    for char in reversed(string):
        rev_string = rev_string + char
    if string == rev_string:
        return True
    else:
        return False


# print(isPalindrome1("abcba"))


# Recursion: Is first letter same as last letter, and is the str in between also a palindrome?
# Time: (we are doing work on N/2 time, so O(N))
# Space: Additional memory used due to additional call stack, so O(N)
def isPalindrome2(string):
    if len(string) < 2:
        return True
    return string[0] == string[len(string) - 1] and isPalindrome2(
        string[1 : len(string) - 1]
    )


# print(isPalindrome2("abcba"))


# Iterate using pointers (Best space -time  complexity!)
# Space: O(1) | Time: O(N)

def isPalindrome3(string):
    left_ptr = 0
    right_ptr = len(string) - 1
    while left_ptr < right_ptr:
        if string[left_ptr] == string[right_ptr]:
            left_ptr += 1
            right_ptr -= 1
        else:
            return False
    return True


# print(isPalindrome3("abcdba"))
