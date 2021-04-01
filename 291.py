###291
#291: Word Pattern II
#Given a pattern and a string str, find if str follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#Examples:
#pattern = "abab", str = "redblueredblue" should return true. 
#pattern = "aaaa", str = "asdasdasdasd" should return true. 
#pattern = "aabb", str = "xyzabcxzyabc" should return false.
#Notes:You may assume both pattern and str contains only lowercase letters.

##time: o(m^n) space: o(n)
##hime: https://www.programmersought.com/article/44737260496/
##Solution: double hashmap+backtracking
'''
solution:
The only difference between this question and the previous question is that the current S is continuous. For continuous S, a more common approach is to use backtracking for brute force search. Divide him into all possible combinations through backtracking, and judge whether the two-way correspondence is consistent. The specific process is as follows:
Given the position i where a pattern is located, the position j where s is located
First, determine whether pattern[i] has an existing mapping. If so, then the word corresponding to s[j:j+k] should be the same as the word corresponding to pattern[i], and then the next level of matching is performed. Otherwise, it proves that it does not meet the matching
If pattern[i] does not have a known mapping, then we should enumerate pattern[i] mapping to any sub string in s starting with j as the index, and backtracking is needed here
'''

class Solution:
    def wordPatternMatch(self, pattern, str):
        def dfs(i,j):
            
            if self.match or i==len(pattern) and j==n:
                self.match = True
                return self.match
            #print(d) ###see below for printed d for case: wordPatternMatch('abab', 'reodresod')
            if i<len(pattern) and j< n:
                p = pattern[i]
                if p in d:
                    w = d[p]
                    if w==str[j:j+len(w)]:
                        dfs(i+1,j+len(w))
                else:
                    for k in range(j,n):
                        w = str[j:k+1]
                        if w not in d.values():
                            d[p] = w
                            dfs(i+1,k+1)
                            d.pop(p) ### backtrack
            return self.match
        
        d = {}; n = len(str); self.match = False
        return dfs(0,0)
tmp =Solution()
tmp.wordPatternMatch('abab', 'reodresod')


#{}
{'a': 'r'}
{'a': 'r', 'b': 'e'}
{'a': 'r', 'b': 'eo'}
{'a': 'r', 'b': 'eod'}
{'a': 'r', 'b': 'eod'}
{'a': 'r', 'b': 'eodr'}
{'a': 'r', 'b': 'eodre'}
{'a': 'r', 'b': 'eodres'}
{'a': 'r', 'b': 'eodreso'}
{'a': 'r', 'b': 'eodresod'}
{'a': 're'}
{'a': 're', 'b': 'o'}
{'a': 're', 'b': 'od'}
{'a': 're', 'b': 'od'}
{'a': 're', 'b': 'odr'}
{'a': 're', 'b': 'odre'}
{'a': 're', 'b': 'odres'}
{'a': 're', 'b': 'odreso'}
{'a': 're', 'b': 'odresod'}
{'a': 'reo'}
{'a': 'reo', 'b': 'd'}
{'a': 'reo', 'b': 'dr'}
{'a': 'reo', 'b': 'dre'}
{'a': 'reo', 'b': 'dres'}
{'a': 'reo', 'b': 'dreso'}
{'a': 'reo', 'b': 'dresod'}
{'a': 'reod'}
{'a': 'reod', 'b': 'r'}
{'a': 'reod', 'b': 're'}
{'a': 'reod', 'b': 'res'}
{'a': 'reod', 'b': 'reso'}
{'a': 'reod', 'b': 'resod'}
{'a': 'reodr'}
{'a': 'reodr', 'b': 'e'}
{'a': 'reodr', 'b': 'es'}
{'a': 'reodr', 'b': 'eso'}
{'a': 'reodr', 'b': 'esod'}
{'a': 'reodre'}
{'a': 'reodre', 'b': 's'}
{'a': 'reodre', 'b': 'so'}
{'a': 'reodre', 'b': 'sod'}
{'a': 'reodres'}
{'a': 'reodres', 'b': 'o'}
{'a': 'reodres', 'b': 'od'}
{'a': 'reodreso'}
{'a': 'reodreso', 'b': 'd'}
{'a': 'reodresod'}




class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        visited_pattern = {}
        visited_str = set()

        def backtrack(i, j):
            if i == len(pattern) and j == len(str):
                return True
            if i == len(pattern) or j == len(str):
                return False
            c = pattern[i]
            if c in visited_pattern:
                mapped_str = visited_pattern[c]
                if str.startswith(mapped_str, j):
                    return backtrack(i + 1, j + len(mapped_str))
                else:
                    return False
            else:
                for end in range(j + 1, len(str) + 1):
                    ss = str[j:end]
                    if ss in visited_str: continue
                    visited_pattern[c] = ss
                    visited_str.add(ss)
                    if backtrack(i + 1, end):
                        return True
                    del visited_pattern[c]
                    visited_str.remove(ss)
                return False

        return backtrack(0, 0)
