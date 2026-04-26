class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        n = len(matrix)
        m = len(matrix[0])
        left = top = 0
        right, bottom = m,n
        res = []
        while left < right and top < bottom: 
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                return res

            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

        """
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9,10,11,12]]
        """