'''
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap
the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by
only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to
combine them.

Example 1:

Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

Note:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
 '''

#requirement:
#input string s
# n_string_size = len(s) <= 1000 -> N 
# n_dict_size = len(dict) <= 100 -> M
#solution 1: line scan
# sort dict by length 
# initilize an array to store the lines, say lines 
# iterate the input string from index 0 to n_string_size
# for index i, check if s[i:] startwith with word in dict
# if word j meet above if condition, create two lines at i (for open "<b>"), and i + len(word j)  for (close <b/>)
# after the for loop, calculate the cum sum of array lines 
# generate the results 

#complexity:  time  O( N * M), space O(N)
#s = "aaabbcc"
#dict = ["aaa","aab","bc"]
#lines = [0,0,0,0,0,0,0,0] -> [1,0,0,-1,0,0,0] -> [1,1,0,-1,-1,0,0] -> [1,1,0,-1,1,0,-1]
# cum lines  = [1,2,2,1,2,2,1]
#
class text:
    def addBoldTag(self, s, dict) -> str:
        dict.sort(key = len, reverse = 1)
        is_bold = [0] * (len(s) + 1) 
        end = 0
        for i in range(len(s)):
            for word in dict:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
                    break
            is_bold[i] = end > i

        ret = []
        i = 0
        while i < len(s):
            if not is_bold[i]:
                ret.append(s[i])
                i += 1
            else:
                j = i
                while is_bold[i]:
                    i += 1
                ret.append("<b>" + s[j:i] + "</b>")
        return "".join(ret)
       
'''       
t = text()
#t.addBoldTag('avvaabbbcca', ['cca','aab','av', 'kaad'])
print(t.addBoldTag('aaavdarefavafdddvvvvaaaacacerevca', ['cac','aereab','avc', 'vvaa']))
'''    
             
class text: 
    def addBoldTag(self, s, dict):  # s is the input string
        N = len(s)
        lines = [0] * (N  + 2) 
        for i in range(N): 
            for word in dict: 
                if s[i:].startswith(word): 
                    print(i, word, lines)
                    lines[i] += 1 
                    lines[i+len(word)-1] -= 1 
                    print(lines)
        result = [] 
        open = False
        #print(lines)
        for i in range(N): 
            lines[i] += lines[i-1]
            if lines[i] > 0:             
                if not open: 
                    open = True 
                    if result and result[-1] == "</b>": 
                        result.pop()   
                    else:
                        result.append('<b>')
                result.append(s[i])
            else: 
                result.append(s[i])
                if open: 
                    open = False
                    result.append('</b>')
        print(lines, result)
        return ''.join(result) + ('</b>' if open else '') 
t = text()
#t.addBoldTag('avvaabbbcca', ['cca','aab','av', 'kaad'])
print(t.addBoldTag('aavca', ['cac','aereab','avc', 'vvaa']))                
                    
                    
           
