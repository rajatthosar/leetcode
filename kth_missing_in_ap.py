class Solution:
    def get_kth_missing(self, nums: list, k: int) -> int:
        if not nums:
            return -1
        min_elem = min(nums)
        presence = [0] * (max(nums) - min_elem + 1)

        for element in nums:
            presence[element - min_elem] = 1
        missing = -1
        count = 0

        for element_index in range(len(presence)):
            if presence[element_index] == 0:
                missing = element_index + min_elem
                count += 1
            if count == k:
                return missing

        return -1


if __name__ == '__main__':
    nums = [2, 4, 10, 7]
    k = 5
    sol = Solution()
    print(sol.get_kth_missing(nums, k))
