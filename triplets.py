class Solution:
    def count_triplets(self, nums: list, target:int) -> int:
        if not nums:
            return 0
        nums.sort()
        result = 0
        for first_idx in range(len(nums) - 2):
            second_idx = first_idx + 1
            third_idx = len(nums) - 1

            while second_idx < third_idx:
                if nums[first_idx] + nums[second_idx] + nums[third_idx] <= target:
                    result += third_idx - second_idx
                    second_idx += 1
                else:
                    third_idx -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.count_triplets([1, 2, 3, 4, 5], 8))
