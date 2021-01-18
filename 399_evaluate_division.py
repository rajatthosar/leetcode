from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        div_table = defaultdict(dict)
        for equation, value in zip(equations, values):
            div_table[equation[0]][equation[1]] = value
            div_table[equation[1]][equation[0]] = 1 / value
        result = []
        for query in queries:
            if query[0] not in div_table or query[1] not in div_table:
                result.append(-1)
            elif query[0] in div_table and query[1] in div_table:
                result.append(div_table[query[0]][query[1]])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                           queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
