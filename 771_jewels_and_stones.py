class Solution:
    counter = 0

    def count_jewels(self, J:set, S:list)->int:

        if S[0] in J:
            self.counter += 1

        self.counter += self.numJewelsInStones("".join(J), "".join(S[:len(S) // 2]))
        self.counter += self.numJewelsInStones("".join(J), "".join(S[len(S) // 2:]))

    def numJewelsInStones(self, J: str, S: str) -> int:
        if S=="" or J=="" or len(J) * len(S) == 0:
            return 0

        J = set(J)
        S = list(S)

        return self.counter


if __name__ == '__main__':
    solution = Solution()
    J = "aA"
    S = "aAAbb"
    print(solution.numJewelsInStones(J,S))
