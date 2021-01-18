from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        for ast_idx in range(len(asteroids)):
            if asteroids[ast_idx] > 0 and (ast_idx + 1 < len(asteroids)) and asteroids[ast_idx + 1] < 0:
                if abs(asteroids[ast_idx]) > abs(asteroids[ast_idx + 1]):
                    asteroids[ast_idx + 1] = 0
                elif abs(asteroids[ast_idx]) == abs(asteroids[ast_idx + 1]):
                    asteroids[ast_idx], asteroids[ast_idx + 1] = 0, 0
                else:
                    asteroids[ast_idx] = 0
            elif asteroids[ast_idx] < 0 and (ast_idx - 1 > -1) and asteroids[ast_idx - 1] > 0:
                if abs(asteroids[ast_idx]) > abs(asteroids[ast_idx - 1]):
                    asteroids[ast_idx - 1] = 0
                elif abs(asteroids[ast_idx]) == abs(asteroids[ast_idx + 1]):
                    asteroids[ast_idx], asteroids[ast_idx + 1] = 0, 0
                else:
                    asteroids[ast_idx] = 0

        return list(filter(lambda x: x != 0, asteroids))


if __name__ == '__main__':
    sol = Solution()
    print(sol.asteroidCollision([1, -1]))
