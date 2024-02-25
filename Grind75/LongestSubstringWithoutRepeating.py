# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def longest_substring_without_repeating(s):   # sliding window
    if len(s) == 0:
        return s
    l_ptr = 0
    seen = set()
    max_length = 0
    for r_ptr in range(len(s)):
        while s[r_ptr] in seen:
            seen.remove(s[l_ptr])
            l_ptr += 1
        seen.add(s[r_ptr])
        max_length = r_ptr - l_ptr + 1
    return max_length










s = "abcabcbb"
print(longest_substring_without_repeating(s))  # Output: 3