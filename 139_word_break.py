from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        is_present = [False for _ in range(len(s) + 1)]
        is_present[0] = True

        for right_idx in range(1, len(s) + 1):
            for left_idx in range(0, right_idx):
                if is_present[left_idx] and s[left_idx:right_idx] in word_dict_set:
                    is_present[right_idx] = True
                    break
        return is_present[len(s)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak(s="leetcode", wordDict=["leet", "code"]))
