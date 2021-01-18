from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        if d == 0 and arr1 != arr2[:len(arr1)]:
            return 0
        count = 0
        for val1 in arr1:
            if all(abs(val1 - val2) > d for val2 in arr2):
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
