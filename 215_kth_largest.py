import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k > len(nums):
            return -1
        if k == len(nums):
            return min(nums)
        if k == 1:
            return max(nums)

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for element in nums[k + 1:]:
            if element >= min_heap[0]:
                heapq.heappush(min_heap, element)
                heapq.heappop(min_heap)
        return min_heap[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
