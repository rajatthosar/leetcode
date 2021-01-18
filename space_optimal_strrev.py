def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for char_index in range(len(s) // 2):
        temp = s[char_index]
        s[char_index] = s[len(s) - 1 - char_index]
        s[len(s) - 1 - char_index] = temp
    return s


data = ["h", "e", "l", "l", "o"]
print(reverseString(data))
