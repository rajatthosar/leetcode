from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return

        expected = len(nums)
        index = 0
        for num in nums:
            expected ^= index ^ num
            index += 1

        return expected


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0, 1, 2, 3, 5]))
