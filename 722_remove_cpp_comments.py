from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        if not source:
            return []
        result = []
        INLINE_CMT = '//'
        MULT_LINE_CMT_OPEN = '/*'
        MULT_LINE_CMT_CLOSE = '*/'

        for line in source:
            temp_line = ''
            for char_idx in range(stop=len(line) - 1, step=2):
                if line[char_idx:char_idx+2] == INLINE_CMT:
                    break
                temp_line += line[char_idx:char_idx+2]
            result.append(temp_line)

        return result


if __name__ == '__main__':
    sol = Solution()
    src = [
        '// Test code',
        'int main()'
    ]