from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        self.airport_adj_list = defaultdict(list)
        self.result = []
        for (departure, arrival) in tickets:
            heapq.heappush(self.airport_adj_list[departure], arrival)
        self.explore_with_dfs('JFK')
        return self.result[::-1]

    def explore_with_dfs(self, departure: str):
        while len(self.airport_adj_list[departure]) > 0:
            self.explore_with_dfs(heapq.heappop(self.airport_adj_list[departure]))
        self.result.append(departure)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    ))


def temp(tickets):
    airport_idxs = {airport: idx for idx, airport in enumerate(sorted(list(set(sum(tickets, [])))))}
    path_adj_matrix = [[-1] * len(airport_idxs) for _ in range(len(airport_idxs))]
    airport_idxs.update({idx: airport for airport, idx in airport_idxs.items()})
    trips = 0
    result = []

    for src, dest in tickets:
        path_adj_matrix[airport_idxs[src]][airport_idxs[dest]] = 1
        trips += 1
    src_airport = airport_idxs['JFK']
    while len(result) <= trips:
        for dest_idx in range(len(path_adj_matrix[src_airport])):
            if path_adj_matrix[src_airport][dest_idx] == 1:
                if sum(path_adj_matrix[dest_idx]) == (-1 * len(path_adj_matrix[dest_idx])) and len(result) < trips:
                    continue
                path_adj_matrix[src_airport][dest_idx] = -1
                result.append(airport_idxs[dest_idx])
                src_airport = dest_idx
                break

    return result
