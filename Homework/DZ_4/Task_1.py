'''
Напишите функцию для транспонирования матрицы
'''

def transpose_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Создаем пустую транспонированную матрицу
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)