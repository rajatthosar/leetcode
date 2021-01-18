class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 2 and s[0] == s[1]:
            return 2

        power = 1
        max_power = power
        for char_idx in range(1, len(s)):
            ch = s[char_idx]
            if s[char_idx] == s[char_idx - 1]:
                power += 1
            else:
                max_power = max(max_power, power)
                power = 1
        return max(max_power, power)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPower(
        "aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz"))
