class Solution:
    result = []

    def generate(self, numRows: int) -> list:
        if not numRows:
            return []
        result = [[1]]
        if numRows == 1:
            return result
        for row in range(1,numRows):
            result.append([1]+[0 for _ in range(row -1)] + [1])
            for index in range(1, len(result[row]) - 1):
                result[row][index] += result[row - 1][index - 1] + result[row - 1][index]
        return result


if __name__ == '__main__':
    numRows = 5
    sol = Solution()
    print(sol.generate(numRows))
