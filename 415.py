class Solution:
    def calculate(self, A, B): 
        sign, s1, s2 = '', 1 if A[0].isdigit() else -1, 1 if B[0].isdigit() else -1
        A = A.lstrip('-')
        B = B.lstrip('-')
        if s1 == s2: 
            res = self.add(A, B)
            if s1 == -1: sign = '-'
        else:
            if A == B: return '0'
            if not self.compare(A, B): 
                A, B = B, A
                if s2 == -1: sign = '-'
            else: 
                if s1 == -1: sign = '-'
            res = self.reduce(A, B)
        return sign + res 
    
    def add(self, A, B): 
        n1, n2 = len(A), len(B)
        res, d = [], 0
        while n1 or n2 or d:
            v1, v2 = A[n1-1] if n1 else 0, B[n2-1] if n2 else 0 
            cur = int(v1) + int(v2) + d 
            d, v = divmod(cur, 10)
            res.append(v)
            n1 -= 1 
            n2 -= 1 
        return "".join(map(str, res[::-1]))
        
        
    def compare(self, A, B): 
        na, nb = len(A), len(B)
        if na > nb: return True 
        if na < nb: return False 
        for i in range(na): 
            if A[i] > B[i]: 
                return True 
            elif A[i] < B[i]: 
                return False 
        return True  
                
        
    def reduce(self, A, B):
        na, nb, left = len(A), len(B), 0 
        res = []
        while na or nb or left: 
            a = int(A[na-1]) if na else 0 
            b = int(B[nb-1]) if nb else 0 
            cur = a - b - left 
            if cur >= 0:  # 5 -1 >= 2 
                res.append(cur)
                left = 0 
            else: # 1 - 1 < 3
                res.append(cur + 10) 
                left = 1 
            na -= 1 
            nb -= 1 
        return "".join(map(str, res[::-1])).lstrip("0")
        
from collections import deque
t = Solution()
print(t.calculate("10000", '10000'))
