# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid.

# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false

def CompleteParanthesis(s):
    stack = []
    d = {')': '(', ']': '[', '}': '{'}
    if len(s) < 2:
        return False
    for char in s:
        if char in d.values():
            stack.append(char)
        elif d[char] == stack[-1]:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


# print(CompleteParanthesis("()[]{}"))
# print(CompleteParanthesis("({[]})"))
# print(CompleteParanthesis("({[})"))
print(CompleteParanthesis("()"))


