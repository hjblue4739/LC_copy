class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res, d = [], 0
        while n1 or n2 or d:
            v1, v2  = num1[n1-1] if n1 else 0, num2[n2-1] if n2 else 0 
            cur = int(v1) + int(v2) + d 
            d, v = divmod(cur, 10)
            res.append(v)
            n1 = n1 - 1 if n1 else 0 
            n2 = n2 - 1 if n2 else 0 
        return "".join(map(str, res[::-1]))

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
    
    def combine(self, num1, num2): 
        s1, s2 = 1 if num1[0].isdigit() else -1, 1 if num2[0].isdigit() else -1
        if s1 == s2: 
            res = self.add(num1, num2)
            if s1 == -1: res = '-' + res 
        else: 
            res = self.reduce(num2, num1[1:]) if s1 == -1 else self.reduce(num1, num2[1:])
            if s1 == 1: 
                if self.add(res, num2[1:]) != s1: 
                    res = '-' + res
            if s2 == 1: 
                if self.add(res, num1[1:]) != s2: 
                    res = '-' + res
        
        return res 

    def add(self, num1, num2): 
        n1, n2 = len(num1), len(num2)
        res, d = [], 0
        while n1 or n2 or d:
            v1, v2  = num1[n1-1] if n1 else 0, num2[n2-1] if n2 else 0 
            cur = int(v1) + int(v2) + d 
            d, v = divmod(cur, 10)
            res.append(v)
            n1 = n1 - 1 if n1 else 0 
            n2 = n2 - 1 if n2 else 0 
        return "".join(map(str, res[::-1]))
        
    def reduce(self, A, B):
        if A == B: return [0]
        na, nb, left = len(A), len(B), 0 
        res = []
        while na or nb or left: 
            a = int(A[na-1]) if na else 0 
            b = int(B[nb-1]) if nb else 0 
            if a - left >= b:  # 5 -1 >= 2 
                res.append(a-left-b)
                left = 0 
            else: # 1 - 1 < 3 
                if na == 1: 
                    return self.reduce(B,A)#float('Inf')
                else: 
                    res.append(a - left + 10 - b) 
                    left = 1 
            na = na - 1 if na else 0 
            nb = nb - 1 if nb else 0 
        return "".join(map(str, res[::-1]))
            
                
class Solution:
    
    def combine(self, num1, num2): 
        s1, s2 = 1 if num1[0].isdigit() else -1, 1 if num2[0].isdigit() else -1
        if s1 == s2: 
            res = self.add(num1, num2) if s1 == 1 else self.add(num1[1:], num2[1:])
            if s1 == -1: res = '-' + res 
        else: 
            res = self.reduce(num2, num1[1:]) if s1 == -1 else self.reduce(num1, num2[1:])
            if s1 == 1: 
                if self.add(res, num2[1:]) != num1: 
                    res = '-' + res
            if s2 == 1: 
                if self.add(res, num1[1:]) != num2: 
                    res = '-' + res
        
        return res 

    def add(self, num1, num2): 
        n1, n2 = len(num1), len(num2)
        res, d = [], 0
        while n1 or n2 or d:
            v1, v2  = num1[n1-1] if n1 else 0, num2[n2-1] if n2 else 0 
            cur = int(v1) + int(v2) + d 
            d, v = divmod(cur, 10)
            res.append(v)
            n1 = n1 - 1 if n1 else 0 
            n2 = n2 - 1 if n2 else 0 
        return "".join(map(str, res[::-1]))
        
    def reduce(self, A, B):
        if A == B: return [0]
        na, nb, left = len(A), len(B), 0 
        res = []
        while na or nb or left: 
            a = int(A[na-1]) if na else 0 
            b = int(B[nb-1]) if nb else 0 
            if a - left >= b:  # 5 -1 >= 2 
                res.append(a-left-b)
                left = 0 
            else: # 1 - 1 < 3 
                if na == 1: 
                    return self.reduce(B,A)#float('Inf')
                else: 
                    res.append(a - left + 10 - b) 
                    left = 1 
            na = na - 1 if na else 0 
            nb = nb - 1 if nb else 0 
            
      def reduce(self, A, B):
        #A is positive and B is negative 
        #if A == B: return [0]
        na, nb, left = len(A), len(B), 0 
        res = []
        t = deque()
        while na or nb: 
            a = int(A[na-1]) if na else 0 
            b = int(B[nb-1]) if nb else 0 
            t.appendleft(a - b)
            na = na - 1 if na else 0 
            nb = nb - 1 if nb else 0 
        while t and t[0] == 0: t.popleft(t)
        while i, v in enumerate(t): 
            if 
        for i, v in enumerate(t): 
            if 
        res = "".join(map(str, res[::-1]))
        
        return res.lstrip('0')#"".join(map(str, res[::-1]))
t = Solution()
print(t.combine("190909011231125", "-8888877565651000981"))                
        
                
            
            
            
