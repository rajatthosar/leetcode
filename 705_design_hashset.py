class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2048
        self.values = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        hashed_key = key % (self.size - 1)
        for value in self.values[hashed_key]:
            if value == key:
                return
        self.values[hashed_key].append(key)

    def remove(self, key: int) -> None:
        hashed_key = key % (self.size - 1)
        for value_idx in range(len(self.values[hashed_key])):
            if self.values[hashed_key][value_idx] == key:
                if (value_idx == len(self.values[hashed_key]) - 1) and value_idx != 0:
                    self.values[hashed_key].pop()
                elif value_idx == 0 and len(self.values[hashed_key]) == 1:
                    self.values[hashed_key] = []
                else:
                    self.values[hashed_key] = self.values[hashed_key][:value_idx] + self.values[hashed_key][
                                                                                    value_idx + 1:]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashed_key = key % (self.size - 1)
        for value in self.values[hashed_key]:
            if value == key:
                return True
        return False


if __name__ == '__main__':
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.add(3)
    hashset.add(4)
    hashset.add(2049)
    print(hashset.contains(1))
    print(hashset.contains(2))
    print(hashset.contains(3))
    print(hashset.contains(4))
    hashset.remove(4)
    print(hashset.contains(4))
    print(hashset.contains(2049))
