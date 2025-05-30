import numpy as np


def intersects(A1: np.ndarray, A2: np.ndarray, B1: np.ndarray, B2: np.ndarray) -> bool:
    vA = A2 - A1
    vB = B2 - B1
    M = np.array([vA, vB])
    v = A2 + B2
    c = np.dot(np.linalg.inv(M), v)
    return (c[0] >= 0 and c[0] <= 1) and (c[1] >= 0 and c[1] <= 1)


v1 = np.array([1, 0])
v2 = np.array([0, 0])
v3 = np.array([0, 1])
v4 = np.array([0, -1])


print(intersects(v1, v2, v3, v4))
