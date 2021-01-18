from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pop_map = dict()

        for num in nums:

            if num not in pop_map.keys():
                pop_map[num] = 0
            pop_map[num] += 1

            if pop_map[num] > 1:
                return num

        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1, 2, 2, 3, 4]))
