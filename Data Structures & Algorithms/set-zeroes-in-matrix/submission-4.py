class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rset, cset = set(), set()
        
        # Step 1: Identify rows and columns that need to be set to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rset.add(i)  # Store row index
                    cset.add(j)  # Store column index
        
        # Step 2: Modify the matrix in-place
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rset or j in cset:  # Use the correct sets
                    matrix[i][j] = 0