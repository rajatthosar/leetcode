from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return [-1, -1]

        pop_set = set()
        duplicate = 0

        for num in nums:
            if num not in pop_set:
                pop_set.add(num)
            else:
                duplicate = num

        expected = 0
        for expected in range(1, len(nums) + 1):
            if expected in pop_set:
                expected += 1
            else:
                break

        return [duplicate, expected]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))
