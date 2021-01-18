from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letter_map = dict()
        for char_idx in range(len(S)):
            if S[char_idx] not in letter_map:
                letter_map[S[char_idx]] = [char_idx, char_idx]
            else:
                letter_map[S[char_idx]][1] = char_idx
        result = []
        intervals = sorted(letter_map.values(), key=lambda idx: idx[0])
        current_start = 0
        current_end = intervals[0][1]

        for interval in intervals:
            if interval[0] > current_end:
                result.append(current_end - current_start + 1)
                current_start = interval[0]
                current_end = interval[1]
            if interval[1] > current_end:
                current_end = interval[1]
        result.append(current_end - current_start + 1)
        return result

    def partitionLabels_v1(self, S: str) -> List[int]:
        last_letter_map = dict()
        for char_idx in range(len(S)):
            last_letter_map[S[char_idx]] = char_idx
        current_end = current_start = 0
        result = []
        for idx, char in enumerate(S):
            current_end = max(current_end, last_letter_map[char])
            if idx == current_end:
                result.append(current_end - current_start + 1)
                current_start = current_end + 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels_v1("ababcbacadefegdehijhklij"))
