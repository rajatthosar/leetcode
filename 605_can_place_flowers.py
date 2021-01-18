from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_copy = flowerbed
        if n == 0:
            return True
        for fl_idx in range(len(flowerbed_copy)):
            if flowerbed_copy[fl_idx] == 1:
                if fl_idx - 1 > -1:
                    flowerbed_copy[fl_idx - 1] = -1
                if fl_idx + 1 < len(flowerbed_copy):
                    flowerbed_copy[fl_idx + 1] = -1
        for fl_idx1 in range(len(flowerbed_copy)):
            if flowerbed_copy[fl_idx1] == 0:
                flowerbed_copy[fl_idx1] = 1
                if fl_idx1 - 1 > -1:
                    flowerbed_copy[fl_idx1 - 1] = -1
                if fl_idx1 + 1 < len(flowerbed_copy):
                    flowerbed_copy[fl_idx1 + 1] = -1
                n -= 1
                if n == 0:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))
