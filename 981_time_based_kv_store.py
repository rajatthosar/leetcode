from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv_store = defaultdict(list)

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp >= len(self.kv_store[key]):
            self.kv_store[key] += [''] * (2 * timestamp)
        self.kv_store[key][timestamp] = [value]

    # O(n) suboptimal. TODO: implement get with binary search
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ''
        if timestamp >= len(self.kv_store[key]):
            timestamp = len(self.kv_store[key]) - 1
        for index in range(timestamp, -1, -1):
            if self.kv_store[key][index] != '':
                return self.kv_store[key][index]
        return self.kv_store[key][0]


if __name__ == '__main__':
    kv_store = TimeMap()
    kv_store.set('foo', 'bar', 1)
    print(kv_store.get('foo', 1))
    print(kv_store.get('foo', 3))
    kv_store.set('foo1', 'bar1', 1)
    kv_store.set('foo2', 'bar5', 5)
    kv_store.set('foo2', 'bar3', 3)
    print(kv_store.get('foo2', 3))
    print(kv_store.get('foo2', 7))
