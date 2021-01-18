class Solution:

    def isAlienSorted(self, words, order) -> bool:
        order_map = dict()
        if not order or not words:
            return False

        for index, char in enumerate(order):
            order_map[char] = index

        for word_index in range(1, len(words)):
            word1 = list(words[word_index - 1])
            word2 = list(words[word_index])

            while word1 and word2:
                char1 = word1[0]
                char2 = word2[0]
                print(char1, char2)
                print("--")
                if order_map[char1] > order_map[char2]:
                    return False
                elif order_map[char1] < order_map[char2]:
                    break
                else:
                    word1.pop(0)
                    word2.pop(0)

            if word1 and not word2:
                return False

        return True


if __name__ == '__main__':
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    sol = Solution()
    print(sol.isAlienSorted(words,order))