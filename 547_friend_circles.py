from typing import List


class Solution:
    def dfs(self, grid, row, col, rows, cols):
        if grid[row][col] == 0:
            return
        grid[row][col] = 0

        if 0 <= row - 1:
            self.dfs(grid, row - 1, col, rows, cols)
        if 0 <= col - 1:
            self.dfs(grid, row, col - 1, rows, cols)
        if row + 1 < cols:
            self.dfs(grid, row + 1, col, rows, cols)
        if col + 1 < cols:
            self.dfs(grid, row, col + 1, rows, cols)

    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        N = len(M)
        result = 0
        for idx1 in range(N):
            for idx2 in range(idx1, N):
                if idx1 == idx2:
                    continue
                if M[idx1][idx2] == 1:
                    M[idx1] = [edge1 or edge2 for edge1, edge2 in zip(M[idx1], M[idx2])]
                    M[idx2] = [edge1 or edge2 for edge1, edge2 in zip(M[idx1], M[idx2])]

        for isl_idx1 in range(N):
            for isl_idx2 in range(N):
                if M[isl_idx1][isl_idx2] == 1:
                    self.dfs(M, isl_idx1, isl_idx2, N, N)
                    result += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    M = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    print(sol.findCircleNum(M))
