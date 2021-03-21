class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        st = ''
        list_st = []
        for i in self.matrix:
            for j in i:
                st += ' ' + str(j)
            st += '\n'
        return f'{st}'

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            print('Невозможо сложить матрицы разной размерности')
            return 'Erorr'
        else:
            matrix1 = []
            for i in range(len(self.matrix)):
                matrix_temp = []
                for j in range(len(self.matrix[i])):
                    matrix_temp.append(self.matrix[i][j] + other.matrix[i][j])
                matrix1.append(matrix_temp)
            return Matrix(matrix1)

print('матрица1')
matrix1 = Matrix([[2, 3, 4], [4, 5, 6]])
print(matrix1)
print('матрица2')
matrix2 = Matrix([[5, 6, 8], [3, 6, 9]])
print(matrix2)
matrix3 = matrix1 + matrix2
print('сумма двух матриц')
print(matrix3)
