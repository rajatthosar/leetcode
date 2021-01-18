class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogram_map = {
            '1': '1',
            '3': '3',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        encoded = ''.join(list(map(lambda char: strobogram_map[char] if char in strobogram_map else '_', num)))
        return encoded[::-1] == num


if __name__ == '__main__':
    sol = Solution()
    print(sol.isStrobogrammatic("69"))
