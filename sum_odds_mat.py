class Solution:
    def oddCells(self, n, m, indices):
        mat = []

        for i in range(n):
            mat.append([0]*m)

        for index_pair in indices:
            row_idx = index_pair[0]
            col_idx = index_pair[1]
            for column in range(m):
                mat[row_idx][column] += 1
            for row in range(n):
                mat[row][col_idx] += 1
        return mat


if __name__ == '__main__':
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    sol = Solution()
    print(sol.oddCells(n,m,indices))