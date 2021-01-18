class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda interval: [interval[1], -interval[0]])
        result_set_len = 2
        current_interval = [intervals[0][1] - 1, intervals[0][1]]
        for (start_time, end_time) in intervals[1:]:

            if current_interval[1] < start_time:
                current_interval = [end_time - 1, end_time]
                result_set_len += 2

            elif current_interval[0] < start_time:
                current_interval = [current_interval[1], end_time]
                result_set_len += 1

        return result_set_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
