#!/usr/bin/python3

from lib import Matrix

print('start')

matrix_1 = Matrix(1,2,3,4)
matrix_2 = Matrix(1,2,3,4)
matrix_3 = matrix_1.add(matrix_2)

print('Test 1')
print(matrix_3.x)
print(matrix_3.y)
print(matrix_3.z)
print(matrix_3.w)

matrix_4 = matrix_1.product(matrix_2)

print('Test 2')
print(matrix_4.x)
print(matrix_4.y)
print(matrix_4.z)
print(matrix_4.w)
