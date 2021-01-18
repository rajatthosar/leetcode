from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        sorted_intervals = sorted(intervals, key=lambda slot: slot[0])
        meeting_rooms = [sorted_intervals[0][1]]

        heapq.heapify(meeting_rooms)

        for times in sorted_intervals[1:]:
            start_time = times[0]
            end_time = times[1]

            if start_time >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, end_time)

        return len(meeting_rooms)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
