class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        if not arr1:
            return arr2
        freq_map = dict()
        ordered_keys = []

        result = []
        for element in arr1:
            if element not in freq_map.keys():
                freq_map[element] = 1
                ordered_keys.append(element)
            else:
                freq_map[element] += 1
        ordered_keys.sort()

        for element in arr2:
            result += [element] * freq_map[element]
            del freq_map[element]
            ordered_keys.remove(element)

        for value in ordered_keys:
            result += [value] * freq_map[value]
            del freq_map[value]

        return result


if __name__ == '__main__':
    arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
    arr2 = [2, 42, 38, 0, 43, 21]
    sol = Solution()
    print(sol.relativeSortArray(arr1, arr2))
