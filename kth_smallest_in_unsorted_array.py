class Solution:
    def get_pivot_index(self, nums: list, left: int, right: int) -> int:
        pivot = nums[right]
        pivot_index = left

        for arr_index in range(left, right):
            if nums[arr_index] <= pivot:
                nums[arr_index], nums[pivot_index] = nums[pivot_index], nums[arr_index]
                pivot_index += 1
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        return pivot_index

    def get_kth_smallest(self, nums: list, k: int, left: int, right: int) -> int:
        if 0 < k <= right - left + 1:
            pivot_index = self.get_pivot_index(nums, left, right)
            if pivot_index - left == k - 1:
                return nums[pivot_index]
            elif pivot_index - left > k - 1:
                return self.get_kth_smallest(nums, k, left, pivot_index - 1)
            else:
                return self.get_kth_smallest(nums, k - 1 - pivot_index + left, pivot_index + 1, right)
        return -1


if __name__ == '__main__':
    nums = [2, 1, 4, 3, 7, 6, 5]
    k = len(nums) // 2
    if len(nums) % 2 == 1:
        k += 1
    k = 2
    sol = Solution()
    print(sol.get_kth_smallest(nums, k, 0, len(nums) - 1))
