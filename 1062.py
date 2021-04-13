

#LeetCode 1062. Longest Repeating substring
class solution: 
    ###O(n^3)
    def longestReSubString(self, s): 
        d = set()
        res = 0
        for i in range(len(s)): 
            for j in range(i): 
                if s[j:i+1] in d:
                    res = max(res, i-j+1)
                else:
                    d.add(s[j:i+1])
        return res
    
    ###o(n^2)
    def longestReSubString(self, s): 
        n = len(s)
        res = 0
        dp = [[1]*n for _ in range(n)]
        for i in range(1, len(s)): 
            for j in range(1, i): 
                if s[j] == s[i]:
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res, dp[i][j])
        return res
    
    
tmp = solution()
tmp.longestReSubString("aabcaabdaab")
