def solution(seq: list) -> int:
    counter = 0
    max = 0
    for index in range(len(seq)):
        for sub_index in range(0, index):
            if seq[sub_index] % seq[index] == 0:
                counter += 1
        if max < counter:
            max = counter
        counter = 0
    return max


array = [8, 1, 28, 4, 2, 6, 7, 1, 2, 3, 1, 3, 2, 2, 1, 52, 5, 6, 4, 5, 5, 56, 64, 5]
print(solution(array))
