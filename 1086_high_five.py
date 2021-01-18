class Solution:
    def highFive(self, items):
        average_map = dict()
        result = []
        if not items:
            return []

        for item in items:
            if item[0] not in average_map.keys():
                average_map[item[0]] = [item[1]]
            else:
                average_map[item[0]].append(item[1])

        for key in average_map.keys():
            result.append([key,sum(sorted(average_map[key], reverse=True)[:5]) // 5])

        return result


if __name__ == '__main__':
    array = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    sol = Solution()
    print(sol.highFive(array))