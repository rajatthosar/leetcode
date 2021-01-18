from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        result = sorted(points, key=lambda pt: pt[0] ** 2 + pt[1] ** 2)[:K]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2], [2, -2]], K=2))
