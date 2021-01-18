def get_lcm(nums):
    from math import gcd
    lcm = nums[0]
    for num_idx in range(1, len(nums)):
        lcm *= nums[num_idx] // gcd(lcm, nums[num_idx])
    return lcm


def solution(X, Y):
    # write your code in Python 3.6
    '''
    X = [1,1,2]
    LCM for Y = 6
    multiply X[i]* LCM(Y) /Y[i]
    X = [2, 3, 4]
    4
    Y = [3,2,3]
    '''
    LIMITER = (10 ** 9) + 7
    lcm = get_lcm(Y)
    ways = 0
    num_map = dict()

    for idx in range(len(X)):
        X[idx] *= int(lcm / Y[idx])
        ways = ways + num_map.get(lcm - X[idx], 0)
        ways %= LIMITER
        num_map[X[idx]] = num_map.get(X[idx], 0) + 1
    return ways


print(solution([1, 1, 2], [3, 2, 3]))
