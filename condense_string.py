from collections import OrderedDict


class Solution:
    def countDupFrequency(self, string: str) -> str:
        letter_freq_map = OrderedDict()
        for char in string:
            if char not in letter_freq_map:
                letter_freq_map[char] = 0
            letter_freq_map[char] += 1
        result = ''
        for character, frequency in letter_freq_map.items():
            result += "{}{}".format(character, frequency)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDupFrequency("aaaaaabbbbbbbccccccss"))
