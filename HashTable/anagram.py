# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t): # Solve using hash map. Both hash maps should be equal
    d_s = {}
    for ch in s:
        if ch in d_s.keys():
            d_s[ch] += 1
        else:
            d_s[ch] = 1
    d_t = {}
    for ch in t:
        if ch in d_t.keys():
            d_t[ch] += 1
        else:
            d_t[ch] = 1
    return d_s == d_t

print(isAnagram("anagram", "nagarm"))


