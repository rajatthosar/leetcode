class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.numbers.keys():
            self.numbers[number] = 0
        self.numbers[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.numbers.keys():
            diff = value - key
            if diff != key:
                if (value - key) in self.numbers.keys():
                    return True
            elif self.numbers[key] > 1:
                return True
        return False


if __name__ == '__main__':
    ts = TwoSum()
    ts.add(3)
    ts.add(2)
    ts.add(1)
    print(ts.find(2))
    print(ts.find(3))
    print(ts.find(4))
    print(ts.find(5))
    print(ts.find(6))
