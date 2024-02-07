# https://leetcode.com/problems/first-bad-version/description/
def isBadVersion(version):
    # This function is assumed to be provided, it determines whether a version is bad or not.
    # For demonstration purposes, let's assume a simple implementation.
    return version >= 4  # Assume version 4 and beyond are bad versions.


def firstBadVersion(n: int) -> int:  # Binary search implementation O(logN)
    start = 1
    end = n
    while start < end:
        print(start, end)
        mid = (start + end) // 2
        if isBadVersion(mid) is True:
            end = mid
        else:
            start = mid + 1
    return start


print(firstBadVersion(7))