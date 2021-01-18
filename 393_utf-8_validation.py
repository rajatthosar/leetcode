from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return True
        first = str(bin(data[0]))[2:]
        ones = bit_idx = 0
        while first[bit_idx] == '1' and bit_idx < len(first):
            ones += 1
            bit_idx += 1
        if ones > len(data) - 1:
            return False
        for encoded_string in data[1:]:
            if str(bin(encoded_string))[2:4] != '10':
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.validUtf8([197, 130, 1]))
