#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.
class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRowZero = True

        # Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                firstColZero = True

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to 0 using markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to 0
        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        # Set first column to 0
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0
        
