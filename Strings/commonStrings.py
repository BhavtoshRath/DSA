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
# print(commonCharacters2(strings))

def commonCharacters3(strings):
    set_strings = [set(string) for string in strings]
    smallest_string = list(min(set_strings, key=len))
    print(smallest_string)
    for char in smallest_string:
        for set_string in set_strings:
            if char not in set_string:
                if char in smallest_string:
                    smallest_string.remove(char)
    return smallest_string


strings = ["abc", "bcd", "cbad"]
strings = ["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]
print(commonCharacters3(strings))

# ['f', '*', '!', 'a', '&']
# ['*', '!', '&']

# ['a', '!', '*', '&', 'f']
# ['!', '&']


