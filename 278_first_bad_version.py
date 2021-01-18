def isBadVersion(version):
    return True if version in [1] else False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n

        while first < last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1

        return first


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstBadVersion(0))
