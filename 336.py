class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup = {w: i for i, w in enumerate(words)}
        result = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, pos = w[:j], w[j:]
                if j != 0 and pre == pre[::-1] and pos[::-1] != w and pos[::-1] in lookup:
                    result.append([lookup[pos[::-1]], i])
                if pos == pos[::-1] and pre[::-1] != w and pre[::-1] in lookup:
                    result.append([i, lookup[pre[::-1]]])
        return result
    
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        #1 <= words.length <= 5000
        
        ##brutal force
        # O(n^2*m); Space(m)
        n = len(words)
        isPalin = lambda x: x[:len(x) // 2] == x[len(x)//2+1:][::-1] if len(x) & 1 else x[:len(x) // 2] == x[len(x)//2:][::-1]
        res = []
        for i, j in itertools.combinations(range(n), 2): 
            if isPalin(words[i] + words[j]): res.append([i,j])
            if isPalin(words[j] + words[i]): res.append([j,i])                
        return res
    
       
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {w[::-1]:j for j, w in enumerate(words)}
        n = len(words)
        res = set()
        isPalin = lambda x: x == x[::-1]
        for j, w in enumerate(words): #n
            for i in range(len(w)+1): #m
                a, b = w[:i], w[i:]
                if (i >= len(w) or w[0] == w[i-1]) and b in d and j != d[b] and isPalin(a):
                    res.add((d[b], j))
                if (i >= len(w) or w[i] == w[-1]) and a in d and j != d[a] and isPalin(b):
                    res.add((j, d[a]))
        return res
                     
                
            
   
