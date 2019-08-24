def rotate(matrix):
    _matrix = []
    for index, ele in enumerate(matrix):
        i = len(matrix) - 1
        _matrix.append([])
        while i >= 0 :
            _matrix[index].append(matrix[i][index])
            i -= 1
    return _matrix

