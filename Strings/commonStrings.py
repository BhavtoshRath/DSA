def commonCharacters(strings):
    char_set = set(strings[0])
    for string in strings[1:]:
        char_set = char_set.intersection(set(string))
    return list(char_set)


strings = ["abc", "bcd", "cbaccd"]

print(commonCharacters(strings))