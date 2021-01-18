class Solution:
    def get_lexical_max_substring(self, string: str) -> str:
        if not string:
            return ''
        largest_char = max(string)
        indices_of_largest = [idx for idx, char in enumerate(string) if char == largest_char]
        if len(indices_of_largest) == 1:
            return string[indices_of_largest[0]:]
        result = ''
        for index in indices_of_largest:
            result = max(result, string[index:])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.get_lexical_max_substring('bacca'))
