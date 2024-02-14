
def addBinary(a: str, b: str) -> str:
    # Initialize variables to store the result and carry
    result = []
    carry = 0

    # Traverse the binary strings from right to left
    i, j = len(a) - 1, len(b) - 1

    # Iterate until both strings are exhausted
    while i >= 0 or j >= 0:
        # Get the current digits or 0 if already exhausted
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Calculate the sum of the current digits and the carry
        # The sum will be 0, 1, 2, or 3 (in binary)
        current_sum = digit_a + digit_b + carry

        # Append the least significant bit of the sum to the result
        result.append(str(current_sum % 2))

        # Update the carry for the next iteration
        carry = current_sum // 2

        # Move to the next digits in both strings
        i -= 1
        j -= 1

    # If there is still a carry, append it to the result
    if carry:
        result.append(str(carry))

    # Reverse the result and join to get the final binary string
    return ''.join(result[::-1])


def addBinary1(a, b):
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >=0 or j >= 0:
        dig_a = int(a[i]) if i >=0 else 0
        dig_b = int(b[j]) if j >=0 else 0
        current_sum = dig_a + dig_b + carry  # imp
        carry = current_sum // 2
        result.append(str(current_sum%2))
        i -=1
        j -=1
    if carry == 1:
        result.append(str(carry))
    return "".join(result[::-1])


print(addBinary1("1101", "101"))

