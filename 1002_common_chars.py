class Solution:
    def commonCharsWithCounter(self, A) :
        from collections import Counter
        word = Counter(A[0])
        for i in range(1, len(A)):
            word = word & Counter(A[i])

        ans = []
        for i in word.keys():
            if word[i] > 1:
                for k in range(word[i]):
                    ans.append(i)
            else:
                ans.append(i)
        return ans

    def commonChars(self, A: list) -> list:
        if not A:
            return []
        alpha_freq = [0] * 26
        words = len(A)
        if words < 2:
            return A

        result = []

        for char in A[0]:
            if char.isalpha:
                alpha_freq[ord(char) - 97] += 1

        for word in A[1:]:
            temp_freq = [0] * 26
            for char in word:
                if char.isalpha:
                    temp_freq[ord(char) - 97] += 1
            for index in range(26):
                alpha_freq[index] = min(alpha_freq[index], temp_freq[index])

        for al_index in range(26):
            # if alpha_freq[al_index] > 0:
            result += [(chr(97 + al_index))] * alpha_freq[al_index]

        return result


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    sol = Solution()
    print(sol.commonCharsWithCounter(A))
