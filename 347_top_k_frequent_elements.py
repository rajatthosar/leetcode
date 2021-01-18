from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freq_map = dict()
        freq_bins = [[] for _ in range(len(nums) + 1)]
        result = []

        for number in nums:
            if number not in freq_map:
                freq_map[number] = 0
            freq_map[number] += 1

        for number, frequency in freq_map.items():
            freq_bins[frequency].append(number)

        index = len(freq_bins) - 1
        while len(result) < k and index > 0:
            if freq_bins[index]:
                for item in freq_bins[index]:
                    result.append(item)
            index -= 1

        return result[:k]


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1, 2], 2))
