'''
249. Group Shifted Strings (Medium)
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

'''
import collections
class Solution:
    def groupStrings(self, strings):
        d = collections.defaultdict(list)
        for s in strings:
            key = tuple(((ord(s[i]) - ord(s[i-1])) % 26) for i in range(1, len(s)))
            d[key].append(s)
            
        return list(d.values())
    
t=Solution()
print(t.groupStrings(['abc','cde','a', 'z', 'cd','xy']))
