# Amazon interview: 2/9/24

# We have a platform called AnnotationHub where we can collect annotations for each document.
# For simplicity, we assume the annotations are binary numbers {0, 1} meaning negative or positive document quality.
# We also assume the output of an annotation task is a matrix with m rows and n columns representing annotation results for m products by n annotators.
# By the way of AnnotationHub backend algorithm works,  we know the rows of the matrix are sorted.
# Our goal is to find the product (row) with the highest fraction of positive annotations.
# If multiple products are tied for the highest positive rate, we can output any of them. Example:

# 0,1,1,1,1,1
# 0,0,1,1,1,1
# 1,1,1,1,1,1
# 0,0,0,0,0,1

# Starting from 0 index, product 2 has the positive rate of 1


def binary_search(mat):  # shape: m*n
    result = []
    n_row = len(mat)
    for m in range(0, n_row):  # [0,1,2,....n_row-1]
        row = mat[m]
        left_ptr = 0
        right_ptr = n_row - 1
        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if row[mid] == 1:
                right_ptr = mid
            else:
                left_ptr = mid + 1

        result.append(left_ptr)

    return (result.index(max(result)))  # timecomplexity: m*log(n) + m




