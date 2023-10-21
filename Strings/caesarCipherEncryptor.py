def caesarCipherEncryptor(string, key):
    result = ""
    for char in string:
        if ord(char) < 97 or ord(char) > 122:
            return False
        pos = ord(char) + key
        if pos > 122:
            pos = 97 + (pos - 122)%26 - 1  # imp logic here
        result += chr(pos)
    # Write your code here.
    return result


print(caesarCipherEncryptor('zbc', 4))


# a:97
# b:122


