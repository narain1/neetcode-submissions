class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        y1, y2 = 0, h

        while y1 < y2:
            m1 = (y1 + y2) // 2

            if 0 <= m1 < h and matrix[m1][0] <= target <= matrix[m1][w - 1]:
                x1, x2 = 0, w
                while x1 < x2:
                    m2 = (x1 + x2) // 2
                    if matrix[m1][m2] == target:
                        return True
                    elif matrix[m1][m2] < target:
                        x1 = m2 + 1
                    else:
                        x2 = m2
                return False

            elif 0 <= m1 < h and target < matrix[m1][0]:
                y2 = m1
            
            elif 0 <= m1 < h and target > matrix[m1][w - 1]:
                y1 = m1 + 1
            elif m1 >= h:
                y2 = m1
            else:
                return False
        return False