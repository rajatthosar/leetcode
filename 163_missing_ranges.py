from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [str(lower) + "->" + str(upper)]

        expected = lower
        result = []

        for number in nums:
            if number != expected:
                result.append(str(expected)) if number - 1 == expected else result.append(
                    str(expected) + "->" + str(number - 1))
            expected = number + 1

        if nums[-1] != upper:
            result.append(str(nums[-1] + 1) + "->" + str(upper))

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMissingRanges([0, 1, 3, 50, 75], lower=0, upper=99))
