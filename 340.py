'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = 0
        start, end = 0, 0
        result = 0
        d = {}
        while end < len(s):
            c = s[end]
            d[c] = d.get(c, 0) + 1
            if d[c] == 1:
                count += 1
            end += 1
            while count > k and start < len(s):
                curr = s[start]
                if curr in d:
                    d[curr] -= 1
                    if d[curr] == 0:
                        count -= 1
                start += 1
            result = max(result, end - start)
        return result
