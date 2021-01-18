from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return len(arr[0])
        max_len = [0] * len(arr)

        for str_idx in range(len(arr)):
            unique_chars = set(arr[str_idx])
            if len(unique_chars) != len(arr[str_idx]):
                continue
            max_len[str_idx] = len(unique_chars)
            for selected_idx in range(str_idx + 1, len(arr)):
                if len(unique_chars.intersection(set(arr[selected_idx]))) == 0:
                    unique_chars = unique_chars.union(set(arr[selected_idx]))
                max_len[str_idx] = max(max_len[str_idx], len(unique_chars))
        return max(max_len)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxLength(["a", "abc", "d", "de", "def"]))
