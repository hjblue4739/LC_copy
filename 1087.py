leetcode 1087
'''
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  
If there is more than one option, then curly braces delimit the options.  
For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]
Note:1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
'''

class solution:
    def brace(self, s): 
        n = len(s); res = []
        def dfs(i, path):
            
            if i == n:
                res.append(path)
                return 
            v = s[i]
            if v == "{":
                j = i + 1
                while s[j] != "}": 
                    j += 1
                for k in s[i+1:j].split(','):
                    dfs(j+1, path + k)
            elif v.isalpha():
                dfs(i+1, path + v)
            return res
        return dfs(0, '')
tmp =solution()
tmp.brace('a{b,p,k,h,t}ab')
