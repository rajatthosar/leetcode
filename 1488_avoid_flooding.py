from typing import List
from collections import deque


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        if not rains:
            return []
        lakes = set()
        to_clean = deque([])
        result = [1] * len(rains)
        for idx in range(len(rains)):
            if rains[idx] > 0:
                result[idx] = -1
                if len(to_clean) >= len(lakes):
                    while lakes:
                        result[to_clean.popleft()] = lakes.pop()
                    to_clean = deque([])
                elif len(to_clean) > 0 and rains[idx] in lakes:
                    result[to_clean.popleft()] = rains[idx]
                    lakes.remove(rains[idx])
                elif rains[idx] in lakes:
                    return []
                lakes.add(rains[idx])
            else:
                to_clean.append(idx)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.avoidFlood([3, 5, 4, 0, 1, 0, 1, 5, 2, 8, 9]))
