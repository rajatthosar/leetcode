from typing import List


class Solution:
    def dfs(self, grid, x, y, rows, cols):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'

        if x + 1 < rows:
            self.dfs(grid, x + 1, y, rows, cols)
        if x - 1 >= 0:
            self.dfs(grid, x - 1, y, rows, cols)
        if y + 1 < cols:
            self.dfs(grid, x, y + 1, rows, cols)
        if y - 1 >= 0:
            self.dfs(grid, x, y - 1, rows, cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, rows, cols)
                    count += 1

        return count


if __name__ == '__main__':
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1"]
    ]
    print(sol.numIslands(grid))
