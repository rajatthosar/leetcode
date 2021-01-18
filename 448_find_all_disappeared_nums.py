from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        num_set = set(nums)
        result = []
        for expected in range(1, len(nums) + 1):
            if expected not in num_set:
                result.append(expected)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
