def reverseVowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = list(s)
    revIdx = len(s) - 1
    charIdx = 0
    while charIdx < revIdx:
        if s[charIdx].lower() in vowels and s[revIdx].lower() in vowels:
            temp = s[charIdx]
            s[charIdx] = s[revIdx]
            s[revIdx] = temp
            charIdx += 1
            revIdx -= 1
        if s[charIdx].lower() not in vowels:
            charIdx += 1
        if s[revIdx].lower() not in vowels:
            revIdx -= 1

    return "".join(s)


data = "Euston saw I was not Sue."
print(reverseVowels(data))
