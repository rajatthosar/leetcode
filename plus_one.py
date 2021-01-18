class Solution:
    def plusOne(self, digits: list) -> list:
        if digits:
            last_idx = len(digits) - 1
            digits[last_idx] += 1
            if digits[last_idx] > 9:
                digits[last_idx] -= 10
                carry = 1
                last_idx -= 1
                while carry != 0 and last_idx >= 0:
                    digits[last_idx] += carry
                    carry = max(digits[last_idx] - 9, 0)
                    digits[last_idx] %= 10
                    last_idx -= 1

            if digits[0] == 0 and carry != 0:
                digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    digits = [9,9]
    sol = Solution()
    print(sol.plusOne(digits))