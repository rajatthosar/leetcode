from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        subseq_len = 1

        for out_idx in range(len(nums)):
            count = 1
            greatest = nums[out_idx]
            for in_idx in range(out_idx + 1, len(nums)):
                if (nums[out_idx] < nums[in_idx]) and nums[in_idx] > greatest:
                    count += 1
                    greatest = nums[in_idx]
            subseq_len = max(subseq_len, count)

        return subseq_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 4]))
