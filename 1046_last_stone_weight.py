class Solution:
    def insert(self, stones, init_idx, last_idx, val):
        # reverse PQ implementation
        mid_idx = (init_idx + last_idx) // 2
        if val == stones[mid_idx]:
            stones.insert(mid_idx, val)
        elif last_idx - init_idx == 1:
            stones.insert(last_idx, val)
            if stones[last_idx] < stones[last_idx+1]:
                stones[last_idx], stones[last_idx+1] = stones[last_idx + 1], stones[last_idx]
        elif val < stones[mid_idx]:
            self.insert(stones, mid_idx, last_idx, val)
        elif val > stones[mid_idx]:
            self.insert(stones, init_idx, mid_idx, val)
        return stones

    def get_stone(self, stones: list) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        else:
            while stones[0] != 0:
                val = stones.pop(0)
                if stones:
                    self.insert(stones, 0, len(stones) - 1, abs(val - stones[0]))
            if not stones:
                return val
            else:
                stones.pop(0)
                return self.get_stone(stones)

    def lastStoneWeight(self, stones: list) -> int:
        stones.sort(reverse=True)
        last_stone = self.get_stone(stones)
        return last_stone


if __name__ == '__main__':
    stones = [7, 6, 7, 6, 9]
    sol = Solution()
    print(sol.lastStoneWeight(stones))
