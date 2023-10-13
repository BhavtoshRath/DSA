def commonCharacters(strings):
    char_set = set()
    for string in strings:
        char_set = char_set.intersection(set(string))
    return []


strings = ["abc", "bcd", "cbaccd"]

print(commonCharacters(strings))