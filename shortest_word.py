class Solution:
    def shortestDistance(self, words, word1, word2):
        hashed_word1 = hash(word1)
        hashed_word2 = hash(word2)
        w1_min = None
        w1_max = -1
        w2_min = None
        w2_max = -1

        for index in range(len(words)):
            if hash(words[index]) == hashed_word1:
                if w1_min is None:
                    w1_min = index
                else:
                    w1_max = index

            elif hash(words[index]) == hashed_word2:
                if w2_min is None:
                    w2_min = index
                else:
                    w2_max = index

        return min(abs(w1_min - w2_max), abs(w2_min - w1_max))


if __name__ == '__main__':
    print(1)