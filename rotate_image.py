def rotateImage(a):
    rows = len(a)
    cols = len(a[0])
    for row_idx in range(rows):
        for col_idx in range(row_idx, cols):
            a[row_idx][col_idx], a[col_idx][row_idx] = a[col_idx][row_idx], a[row_idx][col_idx]

    for col_index in range(cols//2):
        for row_index in range(rows):
            a[row_index][col_index], a[row_index][cols - 1 - col_index] = a[row_index][cols - 1 - col_index], a[row_index][col_index]
    return a

if __name__ == '__main__':
    a = [[10, 9, 6, 3, 7],
         [6, 10, 2, 9, 7],
         [7, 6, 3, 8, 2],
         [8, 9, 7, 9, 9],
         [6, 8, 6, 8, 2]]

    print(rotateImage(a))
