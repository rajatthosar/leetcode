class Solution:
    def dfs(self, image, row, col, color, newColor):
        if image[row][col] != color:
            return
        image[row][col] = newColor

        if row + 1 < len(image):
            self.dfs(image, row + 1, col, color, newColor)
        if row - 1 >= 0:
            self.dfs(image, row - 1, col, color, newColor)
        if col + 1 < len(image[0]):
            self.dfs(image, row, col + 1, color, newColor)
        if col - 1 >= 0:
            self.dfs(image, row, col - 1, color, newColor)

    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:

        color = image[sr][sc]
        mask = -1
        self.dfs(image, sr, sc, color, mask)
        self.dfs(image, sr, sc, mask, newColor)

        return image


if __name__ == '__main__':
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    sol = Solution()
    print(sol.floodFill(image,sr, sc, newColor))