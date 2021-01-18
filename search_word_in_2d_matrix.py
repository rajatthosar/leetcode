class Solution:
    result = []

    def dfs(self, grid, row, col, word, word_index, rows, cols):
        if word_index == len(word):
            return True
        if grid[row][col] == -1 or grid[row][col] != word[word_index]:
            return False
        grid[row][col] = -1
        self.result.append([row, col])
        if row + 1 < rows:
            if self.dfs(grid, row + 1, col, word, word_index + 1, rows, cols):
                return True
        if col + 1 < cols:
            if self.dfs(grid, row, col + 1, word, word_index + 1, rows, cols):
                return True

    def find_word(self, grid, word):
        if not grid or not word:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if len(self.result) == len(word):
                    return self.result
                else:
                    self.result.clear()
                    self.dfs(grid, row, col, word, 0, rows, cols)

        return []


if __name__ == '__main__':
    # grid = [
    #     ['c', 'r', 'c', 'a', 'r', 's'],
    #     ['a', 'b', 'i', 't', 'n', 'b'],
    #     ['t', 'f', 'n', 'n', 't', 'i'],
    #     ['x', 's', 'i', 'i', 'p', 't']
    # ]

    # word = 'catnip'

    grid = [
        ['c', 'r', 'c', 'a', 'r', 's'],
        ['a', 'b', 'i', 't', 'n', 'b'],
        ['t', 'f', 'n', 'n', 't', 'i'],
        ['x', 's', 'c', 'a', 't', 'n'],
        ['x', 's', 'd', 'd', 'e', 'a'],
        ['s', 'q', 'w', 'x', 's', 'p']
    ]

    word = 'catnap'
    sol = Solution()
    print(sol.find_word(grid, word))
