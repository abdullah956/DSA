class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Find all the cells that need to be set to zero
        zero_positions = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        # Step 2: Set the rows and columns to zero
        for (i, j) in zero_positions:
            # Set the entire row to zero
            for col in range(cols):
                matrix[i][col] = 0
            # Set the entire column to zero
            for row in range(rows):
                matrix[row][j] = 0
