from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last_known_zero_idx = -1
        count = result = 0

        if not nums:
            return 0
        for idx in range(len(nums)):
            if nums[idx] == 1:
                count += 1
            else:
                if last_known_zero_idx == -1:
                    count = idx + 1
                else:
                    result = max(result, count)
                    count = idx - last_known_zero_idx
                last_known_zero_idx = idx
        return max(result, count)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 0]))
