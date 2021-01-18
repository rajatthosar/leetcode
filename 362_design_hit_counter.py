from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stream = deque([])
        self.window_start = 0
        self.hits = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.stream or self.window_start < timestamp < self.window_start + 300 :
            self.stream.append((timestamp, 1))
            self.hits += 1
            self.window_start = timestamp
        else:
            if timestamp == self.stream[-1][0]:
                self.stream[-1][1] += 1
            elif timestamp >= self.window_start + 300:
                while timestamp >= self.window_start + 300 or self.stream:
                    self.window_start, discard_hits = self.stream.popleft()
                    self.hits -= discard_hits
                self.hits += 1
                self.stream.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# if __name__ == '__main__':
