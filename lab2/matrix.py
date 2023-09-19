def transpose(matrix):
    result = []
    if len(matrix) == 0:
        return result

    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        result.append(new_row)
    return result

def powers(row, start, end):
    result = []
    for number in row:
        new_row = []
        for power in range(start, end + 1):
            new_row.append(number ** power)
        result.append(new_row)
    return result

def matmul(matrix1, matrix2):

    row1 = len(matrix1)
    column1 = len(matrix1[0]) if matrix1 else 0
    row2 = len(matrix2)
    column2 = len(matrix2[0]) if matrix2 else 0

    if column1 != row2:
        raise ValueError
    new_row = [[0 for col in range(column2)] for row in range(row1)]
    for i in range(row1):
        for j in range(column2):
            for k in range(column1):
                new_row[i][j] += matrix1[i][k]*matrix2[k][j]

    return new_row

def invert(matrix):
    det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    if det == 0:
        raise ValueError
    inv = [[matrix[1][1] / det, -matrix[0][1] / det],
           [-matrix[1][0] / det, matrix[0][0] / det]]
    return inv

def loadtxt(filename):
    matrix = []

    with open(filename, 'r') as file:
        for line in file:
            row = [float(num) for num in line.strip().split('\t')]
            matrix.append(row)

    return matrix