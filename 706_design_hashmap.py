class ValueList:
    def __init__(self):
        self.values = []
        self.KEY_IDX = 0
        self.VAL_IDX = 1

    def get_key_value(self, search_key):
        for stored_key, stored_val in self.values:
            if search_key == stored_key:
                return stored_val
        return -1

    def update_key_value(self, update_key, update_val):
        index = 0
        while index < len(self.values):
            if update_key == self.values[index][self.KEY_IDX]:
                self.values[index][self.VAL_IDX] = update_val
                break
            index += 1

        if index == len(self.values):
            self.values.append([update_key, update_val])

    def remove_key_val(self, remove_key):
        index = 0
        while index < len(self.values):
            if remove_key == self.values[index][self.KEY_IDX]:
                if index == len(self.values) - 1:
                    self.values.pop()
                else:
                    self.values = self.values[:index] + self.values[index + 1:]
                break
            index += 1


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 16
        self.hash_map = [ValueList() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed_key = key % (self.size - 1)
        self.hash_map[hashed_key].update_key_value(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed_key = key % (self.size - 1)
        return self.hash_map[hashed_key].get_key_value(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed_key = key % (self.size - 1)
        return self.hash_map[hashed_key].remove_key_val(key)


if __name__ == '__main__':
    hashmap = MyHashMap()
    hashmap.put(1, 10)
    hashmap.put(2, 7)
    print(hashmap.get(1))
    print(hashmap.get(3))
    hashmap.put(2, 9)
    print(hashmap.get(2))
    hashmap.put(3, 11)
    print(hashmap.get(3))
    hashmap.remove(3)
    print(hashmap.get(3))
