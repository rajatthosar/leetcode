from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        [start1, end1], [start2,end2]
        if start2 < end1 and h2 > h1:
        result.append([start1, h1])

        add if this is the only point
        add larger if there are multiple,
        add 0 at the end

        if two starts are same, replace the current in the sol with the larger one

        4 cases
        totally in
        partially in
        totally out
        overlap

        add first
        then check every element for
            if res_start < el_start <res_end:
                add el_start height if height is greater
            if res_start == el_start and heihgt is greater
                replace res_start and res_end if res_end is smaller
            if el_start > res_end:
                add res_end, 0
                add el_start, heihgt
        '''

        result = [[buildings[0][0], buildings[0][2]]]
        result_end = buildings[0][1]

        for building in buildings[1:]:
            if (result[-1][0] <= building[0] <= result_end) and building[2] > result[-1][1]:
                result.append([building[0], building[2]])
            elif result[-1][0] == building[0] and building[2] > result[-1][1]:
                result[-1] = [building[0], building[2]]
            elif building[0] > result[-1][0]:
                result.append([result_end, 0])
                result.append([building[0], building[2]])
            result_end = building[1] if building[1] > result_end else result_end
        result.append([result_end, 0])
        return result


if __name__ == '__main__':
    sol = Solution()
    sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
