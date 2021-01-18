class Solution:
    def get_kth_smallest(self, nums: list, k: int) -> int:
        if not nums:
            return 0
        index_list = [0]
        delim_count = 0

        for idx in range(len(nums) - 1):
            if nums[idx] == -1:
                delim_count += 1
                if delim_count % 2 == 0:
                    index_list += [idx - 1, idx + 1]
        if delim_count % 2 == 1:
            index_list.append(len(nums) - 1)

        for _ in range(k):
            min_value = float('inf')
            for index in index_list:
                min_value = min(min_value, nums[index])
            for updater_index in range(len(index_list)):
                if updater_index % 2 == 0 and nums[index_list[updater_index] + 1] != -1 and index_list[
                    updater_index] + 1 < len(nums):
                    index_list[updater_index] += 1
                elif updater_index % 2 == 1 and nums[index_list[updater_index] - 1] != -1 and index_list[
                    updater_index] - 1 > 0:
                    index_list[updater_index] -= 1
        return min_value


if __name__ == '__main__':
    nums = [1, 2, 3, -1, 6, 5, 4, -1, 2, 3, 4, 5, 6, -1, 9, 8, 6, 3]
    k = 3
    sol = Solution()
    print(sol.get_kth_smallest(nums, k))
