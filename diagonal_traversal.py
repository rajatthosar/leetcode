class Solution:
    def findDiagonalOrder(self, matrix):
        idx_i, idx_j = 0, 0
        is_switched = False
        result = []
        if len(matrix) * len(matrix[0]) == 0:
            return []

        if type(matrix[0]) != list:
            return matrix

        for lim in range(len(matrix) + len(matrix[0]) - 1):
            if not is_switched:
                idx_i = min(lim, len(matrix) - 1)
                while idx_i >= 0 and idx_j + 1 < len(matrix[0]):
                    idx_j = lim - idx_i
                    result.append(matrix[idx_i][idx_j])
                    idx_i -= 1
            else:
                idx_j = min(lim, len(matrix[0]) - 1)
                while idx_j >= 0 and idx_i + 1 < len(matrix):
                    idx_i = lim - idx_j
                    result.append(matrix[idx_i][idx_j])
                    idx_j -= 1

            is_switched = not is_switched

        return result


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1], [2], [3]
    ]

    print(sol.findDiagonalOrder(matrix))
