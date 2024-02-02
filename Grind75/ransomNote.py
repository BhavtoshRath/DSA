# https://leetcode.com/problems/ransom-note/description/
# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed by using the letters from magazine and false otherwise.

def canConstruct(ransomNote, magazine):  # Use Hash map
    magazine_dict = {}
    for char in magazine:
        if char in magazine_dict:
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1

    for char in ransomNote:
        if char in magazine_dict:
            magazine_dict[char] -= 1
        else:
            return False

    if min(magazine_dict.values()) < 0:
        return False
    else:
        return True


print(canConstruct("aa", "aab"))