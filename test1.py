# O(n) time, O(n) space

def get_duplicate_numbers(nums: []) -> []:
    if not nums:
        return []
    num_set = set()
    result = []
    for number in nums:
        if number not in num_set:
            num_set.add(number)
        else:
            result.append(number)
    return result


# O(nlogn) suboptimal , O(1) space
def get_duplicate_numbers_sort(nums: []) -> []:
    if not nums or len(nums) == 1:
        return []
    nums.sort()
    result = []
    for num_idx in range(1, len(nums)):
        if nums[num_idx] == nums[num_idx - 1]:
            result.append(nums[num_idx])
    return result


if __name__ == '__main__':
    print(get_duplicate_numbers_sort([11, 2, 2, 234, 42, 4, 4]))
