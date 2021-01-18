from collections import deque
from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        emp_map = {employee.id: employee for employee in employees}

        if id not in emp_map:
            return -1

        power_value = emp_map[id].importance
        subs = deque([])
        for sub_id in emp_map[id].subordinates:
            subs.append(emp_map[sub_id])
        while subs:
            sub = subs.popleft()
            power_value += sub.importance
            for sub_id in sub.subordinates:
                subs.append(emp_map[sub_id])
        return power_value


if __name__ == '__main__':
    emp1 = Employee(1, 5, [2, 3])
    emp2 = Employee(2, 3, [])
    emp3 = Employee(3, 3, [])
    employees = [emp1, emp2, emp3]

    sol = Solution()
    print(sol.getImportance(employees, 1))
