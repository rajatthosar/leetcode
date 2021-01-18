from collections import defaultdict


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''
        letter_map = defaultdict(int)
        for char in S:
            letter_map[char] += 1
        if (len(S) % 2 == 0 and (max(letter_map.values()) > len(S) // 2)) or \
                (len(S) % 2 == 1 and (max(letter_map.values()) > 1 + len(S) // 2)):
            return ''
        result = ''
        frequencies = sorted([[letter, freq] for letter, freq in letter_map.items()],
                             key=lambda letter_freq_pair: letter_freq_pair[1])
        while frequencies:
            for ch_freq_idx in range(len(frequencies) - 1, - 1, -1):
                result += frequencies[ch_freq_idx][0]
                frequencies[ch_freq_idx][1] -= 1
                if frequencies[ch_freq_idx][1] == 0:
                    if ch_freq_idx == len(frequencies) - 1:
                        frequencies.pop()
                    else:
                        frequencies = frequencies[:ch_freq_idx] + frequencies[ch_freq_idx + 1:]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganizeString('aab'))
