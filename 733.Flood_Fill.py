def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]

    if start_color == newColor:
        return image

    def dfs(row, col):
        