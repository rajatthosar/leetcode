import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        heapq.heapify(self.queue)
        self.size = k

        for _ in range(len(self.queue) - k):
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        if len(self.queue) < self.size:
            heapq.heappush(self.queue, val)
        else:
            if val >= self.queue[0]:
                heapq.heappush(self.queue, val)
                heapq.heappop(self.queue)
        return self.queue[0]
    

if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(5))
    print(kthLargest.add(5))
    print(kthLargest.add(8))