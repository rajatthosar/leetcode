from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1
        adj_list = defaultdict(list)

        for edge in trust:
            adj_list[edge[0]].append(edge[1])

        for person in range(1, N + 1):
            if not adj_list[person] or len(adj_list[person]) == 0:
                return person
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findJudge(3, [[1, 3], [2, 3]]))
