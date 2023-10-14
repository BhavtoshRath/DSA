def commonCharacters1(strings):
    char_set = set(strings[0])
    for string in strings[1:]:
        char_set = char_set.intersection(set(string))
    return list(char_set)


strings = ["abc", "bcd", "cbaccd"]

# print(commonCharacters1(strings))


# Time: O(N.M) -N - length of strings, M - length of individual string
# O (C) C- Unique chars across all strings
# D.S: HashMap
def commonCharacters2(strings):
    sol = []
    d = dict()
    for string in strings:
        set_string = set(string)
        for char in set_string:
            if char not in d:
                d[char] = 0
            d[char] += 1
    for char in d:
        if d[char] == len(strings):
            sol.append(char)
    return sol


strings = ["abc", "bcd", "cbaccd"]
print(commonCharacters2(strings))


