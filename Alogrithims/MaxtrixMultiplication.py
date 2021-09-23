def multiply_matrix(a: list[list[int]], b: list[list[int]], m, n):
    x = []

    for i in range(m):
        y = []
        for j in range(n):
            s = 0
            for k in range(m):
                s += a[i][k] * b[k][j]
            y.append(s)
        x.append(y)
    return x


def matrixReshape(mat: list[list[int]], r: int, c: int):
    if r * c != len(mat[0]) * len(mat):
        return mat
    i = 0
    j = 0
    ar = []
    for x in range(r):
        b = []
        for y in range(c):
            if j == len(mat[0]):
                j = 0
                i += 1
            b.append(mat[i][j])
            j += 1
        ar.append(b)
    return ar
