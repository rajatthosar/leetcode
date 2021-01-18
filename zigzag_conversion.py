class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # T(n) = O(n)
        # S(n) = O(n)

        s = list(s)
        bins = [""] * numRows
        index = 0
        is_reversed = False

        if numRows == len(s) or numRows == 1:
            return "".join(s)

        for char in s:
            bins[index] += char
            if index == numRows - 1:
                is_reversed = True
            if index == 0:
                is_reversed = False
            if is_reversed:
                index -= 1
            else:
                index += 1

        result = "".join(bins[idx] for idx in range(len(bins)))
        return result


if __name__ == '__main__':
    string = "AB"
    numRows = 1
    sol = Solution()
    print(sol.convert(string, numRows))
