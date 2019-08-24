def matrixZero(matrix):
    nullifyrows, nullifyColumns = [], []
    for index_i, i in enumerate(matrix):
        for index_j, j in enumerate(i):
            if j == 0:
                nullifyrows.append(index_i)
                nullifyColumns.append(index_j)

    for i in nullifyrows:
        matrix = nullifyRow(i, matrix)

    for i in nullifyColumns:
        matrix = nullifyColumn(i, matrix)

    return matrix


def nullifyRow(index, matrix):
    matrix[index] = [0] * len(matrix[index])
    return matrix

def nullifyColumn(index, matrix):
    for i in range(len(matrix)):
        matrix[i][index] = 0
    return matrix

print(matrixZero([
    [0,2,3,1],
    [1,1,9,8],
    [1,1,1,0]
]))