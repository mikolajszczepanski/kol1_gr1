#!/usr/bin/python3

import unittest
from lib import Matrix

class TestMatrix(unittest.TestCase):

    def test_incorrect_matrix(self):
        with self.assertRaises(ValueError):
          Matrix(
            [0,1,2],
            [4,5,6,5],
            [7,8,9]
            )
    
    def test_incorrect_matrix_2(self):
        with self.assertRaises(ValueError):
          Matrix(
            [0,1,2],
            [4,5,6],
            )
    
    def test_equality_matrix(self):
        m1 = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        m2 = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        self.assertEqual(m1, m2)

    def test_equality_matrix_2(self):
        m1 = Matrix(
            [0,-1,-2],
            [-4,-5,-6],
            [7,8,9]
            )
        m2 = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        self.assertNotEqual(m1, m2)

    def test_equality_matrix_3(self):
        m1 = Matrix(
            [0,1,2,9],
            [4,5,6,9],
            [7,8,9,9],
            [7,8,9,9]
            )
        m2 = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        self.assertNotEqual(m1,m2)

    def test_add_matrix_to_matrix(self):
        m = Matrix(
            [1,1,2],
            [1,0,1],
            [0,-1,0]
            )
        m2 = Matrix(
            [1,5,0],
            [0,4,1],
            [0,0,-2]
            )
        rm = m + m2
        em = Matrix(
            [2,6,2],
            [1,4,2],
            [0,-1,-2]
            )
        self.assertEqual(rm,em)

    def test_sub_matrix_with_matrix(self):
        m = Matrix(
            [1,1,2],
            [1,0,1],
            [0,-1,0]
            )
        m2 = Matrix(
            [1,0,3],
            [0,0,0],
            [0,-1,0]
            )
        rm = m - m2
        em = Matrix(
            [0,1,-1],
            [1,0,1],
            [0,0,0]
            )
        self.assertEqual(rm,em)

    def test_add_number_to_matrix(self):
        m = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        m2 = 1 + m
        rm = Matrix(
            [1,2,3],
            [5,6,7],
            [8,9,10]
            )
        self.assertEqual(rm,m2)

    def test_sub_number_with_matrix(self):
        m = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        m2 = 1 - m
        rm = Matrix(
            [1,0,-1],
            [-3,-4,-5],
            [-6,-7,-8]
            )
        self.assertEqual(rm,m2,msg="result is {0} but should be {1}".format(str(m2),str(rm)))

    def test_sub_matrix_with_number(self):
        m = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        m2 = m - 1
        rm = Matrix(
            [-1,0,1],
            [3,4,5],
            [6,7,8]
            )
        self.assertEqual(rm,m2)

    def test_mul_matrix_with_matrix(self):
        m = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        m2 = Matrix(
            [1,0,-1],
            [-3,-4,-5],
            [-6,-7,-8]
            )
        rm = m * m2
        em = Matrix(
            [-15,-18,-21],
            [-47,-62,-77],
            [-71,-95,-119]
            )
        self.assertEqual(rm,em)

    def test_mul_number_with_matrix(self):
        m = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        rm = 2 * m
        em = Matrix(
            [0,2,4],
            [8,10,12],
            [14,16,18]
            )
        self.assertEqual(rm,em)

    def test_mul_matrix_with_number(self):
        m = Matrix(
            [0,1,2],
            [4,5,6],
            [7,8,9]
            )
        rm = m * 2
        em = Matrix(
            [0,2,4],
            [8,10,12],
            [14,16,18]
            )
        self.assertEqual(rm,em)

if __name__ == '__main__':
    unittest.main()