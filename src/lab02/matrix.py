def transpose(mat):
    for row in mat:
        length = len(mat[0])
        for col in row:
            if len(row) != length:
                raise ValueError("Рваная матрица")
    if mat == []:
        return []
    rows = len(mat) #кол-во строк в первой
    cols = len(mat[0]) #кол-во столбцов в первой
    new_mat = []
    for row in range(cols): #1 -> 3
        new_row = []
        for col in range(rows): #3 -> 1
            new_row.append(mat[col][row])
        new_mat.append(new_row)
    return new_mat
x1 = [[1,2,3]]
x2 = [[1],[2],[3]]
x3 = [[1,2],[3,4]]
x4 = []
x5 = [[1,2],[3]]

def row_sums(mat):
    for row in mat:
        length = len(mat[0])
        for col in row:
            if len(row) != length:
                raise ValueError("Рваная матрица")
    new_mat = []
    for row in mat:
        sum = 0
        for i in row:
            sum += i
        new_mat.append(sum)
    return new_mat

def col_sums(mat):
    for row in mat:
        length = len(mat[0])
        for col in row:
            if len(row) != length:
                raise ValueError("Рваная матрица")
    rows = len(mat)
    cols = len(mat[0])
    for row in range(rows-1):
        new_mat = []
        for col in range(cols):
            new_mat.append(mat[row][col] + mat[row+1][col])
    return new_mat

x1 = [[1,2,3],[4,5,6]]
x2 = [[-1,1],[10,-10]]
x3 = [[0,0],[0,0]]
x4 = [[1,2],[3]]
print(col_sums(x1))
print(col_sums(x2))
print(col_sums(x3))
print(col_sums(x4))