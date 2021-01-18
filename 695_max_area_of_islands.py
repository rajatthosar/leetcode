from typing import List


class Solution:
    def dfs(self, grid, x, y, rows, cols):
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        count = 1
        if x + 1 < rows:
            count += self.dfs(grid, x + 1, y, rows, cols)
        if x - 1 >= 0:
            count += self.dfs(grid, x - 1, y, rows, cols)
        if y + 1 < cols:
            count += self.dfs(grid, x, y + 1, rows, cols)
        if y - 1 >= 0:
            count += self.dfs(grid, x, y - 1, rows, cols)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == 1:
                    area = self.dfs(grid, row_idx, col_idx, rows, cols)
                    max_area = max(area, max_area)

        return max_area


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(sol.maxAreaOfIsland(grid))
