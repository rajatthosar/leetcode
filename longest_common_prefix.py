class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = []
        result_set = []
        last_input = []
        min_len = 100000
        for string in strs:
            s.append(list(string))
            if len(list(string)) < min_len:
                min_len = len(list(string))

        for char_idx in range(min_len):
            for str_no in range(len(s)):
                result_set.add(s[str_no][char_idx])
                last_input.append(s[str_no][char_idx])

            if len(result_set) > char_idx + 1:
                result_set.remove(char for char in last_input)
                break
            last_input.clear()

        return "".join(result_set)


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    sol = Solution()

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [1, 2, 3, 4, 5, 6]

    for i, j in zip(a, b):
        print(str(i) + "  " + str(j))
    # print(sol.longestCommonPrefix(strs))
