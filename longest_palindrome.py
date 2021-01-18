def longestPalindrome(s: str) -> str:
    s = list(s)
    indices = set()
    string = ''

    for head_index in range(len(s)):
        tail_index = len(s) - 1
        while head_index <= tail_index:
            if s[head_index] == s[tail_index]:
                indices.add(head_index)
                indices.add(tail_index)
                head_index += 1
                tail_index -= 1
            else:
                tail_index -= 1
                indices.clear()
        if len(indices) > len(string):
            list(indices).sort()
            string = ''
            for index in indices:
                string += s[index]
        indices.clear()

    return string


data = "abcda"
print(longestPalindrome(data))
