# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        result = n
        for i in range(m):
            left, right = 0, result
            while left < right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(i, mid) == 1:
                    right = mid
                else:
                    left = mid + 1
            result = left
        return result if result != n else -1

    
#time: O(M+N) 
#space: O(1)
 class Solution:
    def leftMostColumnWithOne(self, M: 'BinaryMatrix') -> int:
        m, n = M.dimensions()
        x, y = 0, n - 1  #initial point at the top right corner of the matrix 
        while x < m and -1 < y:
            if M.get(x, y) == 1: 
                    y -= 1  
            x += 1
        return y + 1 if y < n - 1 else -1 
        
    
