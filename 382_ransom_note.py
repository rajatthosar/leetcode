class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if not magazine:
            return False

        letter_map = dict()

        for letter in magazine:
            if letter not in letter_map:
                letter_map[letter] = 0
            letter_map[letter] += 1

        for char in ransomNote:
            if char not in letter_map:
                return False
            letter_map[char] -= 1

        for ch in ransomNote:
            if letter_map[ch] < 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct("ab", "aab"))
