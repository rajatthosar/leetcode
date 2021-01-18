class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word or len(word) == 1:
            return True

        return not word.islower()


if __name__ == '__main__':
    word = "FlaG"
    sol = Solution()
    print(sol.detectCapitalUse(word))
