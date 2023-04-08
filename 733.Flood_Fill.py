def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]

    if start_color == newColor:
        return image
    ###
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != start_color:
            return

        image[row][col] = newColor
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    dfs(sr, sc)
    return image