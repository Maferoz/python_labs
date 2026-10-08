def matrix_check(mat):
    if mat == []:
        return 
    width = len(mat[0])
    for row in mat:
        if len(row) != width:
            raise ValueError("Рваная матрица")

def transpose(mat):
    matrix_check(mat)
    if mat == []:
        return []
    rows = len(mat) #кол-во строк
    cols = len(mat[0]) #кол-во столбцов
    new_mat = []
    for row in range(cols): 
        new_row = []
        for col in range(rows):
            new_row.append(mat[col][row]) # поочередно добавляем значения col и row  для транспонации
        new_mat.append(new_row)
    return new_mat

def row_sums(mat):
    if mat == []:
        return []
    matrix_check(mat)
    new_mat = []
    for row in mat:
        summ = 0
        for i in row:
            summ += i
        new_mat.append(summ)
    return new_mat

def col_sums(mat):
    if mat == []:
        return []
    matrix_check(mat)
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for i in range(rows-1):
        summ = 0
        for j in range(cols-1):
            summ = mat[rows][cols] + mat[rows+1][cols+1]
        result.append(summ)
    return result
x = [[-1, 1 ],[10, -10]]
print(x, col_sums(x))