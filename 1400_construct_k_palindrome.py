from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq_map = Counter(s)
        infractions = 0
        for val in freq_map.values():
            if val % 2 == 0:
                infractions += 1
        return infractions <= k


if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct('abbbccd', 4))
