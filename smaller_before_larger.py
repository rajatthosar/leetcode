class Solution:
    def reorderArray(self, nums: list) -> list:
        if not nums:
            return []
        num_idx = element_counter = 0
        while element_counter < len(nums):
            if nums[num_idx] > 0 and num_idx < len(nums) - 1:
                nums = nums[:num_idx] + nums[num_idx + 1:] + [nums[num_idx]]
            else:
                num_idx += 1
            element_counter += 1
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.reorderArray([5, 2, 7, 4, 3, -8, -10]))
