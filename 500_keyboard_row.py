class Solution:
    def findWords(self, words: list) -> list:
        if not words:
            return []

        result = []
        first_row = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second_row = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third_row = {'z', 'x', 'v', 'c', 'b', 'n', 'm'}

        for word in words:
            if set(word.lower()).issubset(first_row) or set(word.lower()).issubset(second_row) or set(word.lower()).issubset(third_row):
                result.append(word)

        return result


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    sol = Solution()
    print(sol.findWords(words))
