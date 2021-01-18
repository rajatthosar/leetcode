class Solution:
    def countSegments(self, s: str) -> int:
        if not s or s == "":
            return 0
        return len(s.strip().split())


if __name__ == '__main__':
    s = "    asdf asdasdf         "
    sol = Solution()
    print(sol.countSegments(s))