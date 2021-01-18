class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if not rowIndex:
            return []

        pascal = [[1], [1, 1]]

        if rowIndex < 2:
            return pascal[rowIndex]

        for row in range(2, rowIndex + 1):
            temp_array = [1]

            for col in range(len(pascal[row - 1]) - 1):
                temp_array.append(pascal[row - 1][col] + pascal[row - 1][col + 1])
            temp_array.append(1)
            pascal.append(temp_array)

        return pascal[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(4))
