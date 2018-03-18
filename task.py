#!/usr/bin/python3

from lib import Matrix

def main():
    m1 = Matrix(
        [0,1,2],
        [4,5,6],
        [7,8,9]
        )
    m2 = Matrix(
        [5,3,-2],
        [5,5,-10],
        [7,8,8]
        )
    m3 = (( 3 - ( 1 + m1 + m2 - 3 * m1 - m1 ) ) * 2) + 10 + (m1 * m2)
    print(m3)

if __name__ == "__main__":
    main()