from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return False

        sorted_intervals = sum(sorted(intervals, key=lambda slot: slot[0]), [])

        for time_idx in range(1, len(sorted_intervals)):
            if sorted_intervals[time_idx] < sorted_intervals[time_idx - 1]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
