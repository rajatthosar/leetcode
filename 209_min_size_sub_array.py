from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s or (len(nums) == 1 and nums[0] < s):
            return 0
        if max(nums) >= s:
            return 1
        init_ptr = last_ptr = 0
        accumulator = 0
        result = float('inf')
        while last_ptr < len(nums):
            accumulator += nums[last_ptr]
            while accumulator >= s:
                result = min(result, last_ptr - init_ptr + 1)
                accumulator -= nums[init_ptr]
                init_ptr += 1
            last_ptr += 1
        if result == float('inf'):
            result = 0
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
