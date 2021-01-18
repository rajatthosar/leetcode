class Solution:
    def get_unique_array(self, array:list) -> int:
        if not array:
            return 0
        sorted_array = sorted(array)
        result = array[0]
        for num_idx in range(1, len(array)):
            if array[num_idx] == array[num_idx - 1]:
                second_idx = num_idx
