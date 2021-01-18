import numpy as np


def get_quad_roots(a: int, b: int, c: int) -> list:
    diff = (b * b) - 4 * a * c
    if diff < 0:
        return ["Imaginary", "roots"]
    numerator_pos = -b + np.sqrt(diff)
    numerator_neg = -b - np.sqrt(diff)
    root_pos = numerator_pos / (2 * a)
    root_neg = numerator_neg / (2 * a)

    return [np.floor(root_pos), np.floor(root_neg)]


print(get_quad_roots(2, 8, 8))
