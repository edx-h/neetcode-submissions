class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow = False
        firstCol = False
        rowCount = len(matrix)
        colCount = len(matrix[0])

        if self.containsZero(matrix[0]):
            firstRow = True

        if self.containsZero([matrix[r][0] for r in range(rowCount)]):
            firstCol = True

        for c in range(1, colCount):
            if self.containsZero([matrix[r][c] for r in range(rowCount)]):
                matrix[0][c] = 0
        
        for r in range(1, rowCount):
            if self.containsZero([matrix[r][c] for c in range(colCount)]):
                matrix[r][0] = 0
        
        # replace
        for c in range(1, colCount):
            if matrix[0][c] == 0:
                for r in range(rowCount):
                    matrix[r][c] = 0
        
        for r in range(1, rowCount):
            if matrix[r][0] == 0:
                for c in range(colCount):
                    matrix[r][c] = 0

        if firstRow:
            for c in range(colCount):
                matrix[0][c] = 0

        if firstCol:
            for r in range(rowCount):
                matrix[r][0] = 0                
        return

    def containsZero(self, row):
        for v in row:
            if v == 0:
                return True
        
        return False


        