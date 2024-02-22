# https://leetcode.com/problems/flood-fill/description/


def flood_fill(image, sr, sc, new_color):   # dfs on graph
    if image[sr][sc] == new_color:
        return image

    def dfs(row, col, old_color):
        # if image[row][col] != old_color:
        #     print(row, col)
        if row < 0 or row > len(image) or col < 0 or col > len(image[0]) or image[row][col] != old_color: # Not sure about image[row][col] != old_color
            print(row, col)
            return                  # imp concept
        image[row][col] = new_color
        dfs(row - 1, col, old_color)
        dfs(row + 1, col, old_color)
        dfs(row, col - 1, old_color)
        dfs(row, col + 1, old_color)

    dfs(sr, sc, image[sr][sc])
    return image

image = [
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
]
sr, sc = 2, 2
new_color = 2
ctr = 0
result = flood_fill(image, sr, sc, new_color)
for row in result:
    print(row)