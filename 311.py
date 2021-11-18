class Matrix: 
    def mult(self, A, B): 
        if not A or not B: return [[]]
        n, k = len(A), len(A[0])
        m = len(B[0])
        mapA = {(i, j): A[i][j] for i in range(n) for j in range(k) if A[i][j]} 
        mapB = {(i, j): B[i][j] for i in range(k) for j in range(m) if B[i][j]} 
        C = [[0]*m for _ in range(n)]
        for i, j in mapA.keys():   #mapA = {(0,0):1, (1,0):-1, (1,2): 3},  mapB ={(0,0):7, (2,2):1}
            for x, y in mapB.keys(): 
                if j == x: 
                    C[i][y] += mapA[i,j] * mapB[x,y]
        return C 
A = [[ 1, 0, 0], [-1, 0, 3]]
B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]
            
t = Matrix()
C = t.mult(A, B)
print(C)  


'''
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rows, n, cols = len(A), len(A[0]), len(B[0])
        C = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(n):
                if A[i][j] != 0:
                    for z in range(cols):
                        if B[j][z] != 0:
                            C[i][z] += A[i][j] * B[j][z]
        return C
'''    
    
