class Solution:
    def modifyString(self, s: str) -> str:
        letter_lookup = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        char_list = list(s)
        for char_idx in range(len(char_list)):
            if char_list[char_idx] == '?':
                left_char = char_list[char_idx - 1] if (char_idx > 0) and (char_list[char_idx - 1] != '?') else None
                right_char = char_list[char_idx + 1] if (char_idx < len(char_list) - 1) and (
                            char_list[char_idx + 1] != '?') else None

                for letter in letter_lookup:
                    if letter in [left_char, right_char]:
                        continue
                    char_list[char_idx] = letter
                    break
        return ''.join(char_list)


if __name__ == '__main__':
    sol = Solution()
    print(sol.modifyString('j?qg??b'))
