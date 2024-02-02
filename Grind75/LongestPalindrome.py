# https://leetcode.com/problems/longest-palindrome/description/

def LongestPalindrome(s): # Using hash map
    string_dict ={}
    for char in s:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1

    if len(string_dict) == 1:
        return list(string_dict.values())[0]
    else:
        temp = 0
        odd_cntr = 0
        values = string_dict.values()
        for val in values:
            temp += 2*(val//2)
            if val % 2 != 0:
                odd_cntr += 1

        if odd_cntr > 0:
            return temp + 1
        else:
            return temp


print(LongestPalindrome('f'))