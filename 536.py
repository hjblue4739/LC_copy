'''
https://www.cnblogs.com/grandyang/p/6793904.html
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
'''
class treeNode: 
    def __init__(self, x = 0, left = None , right = None): 
         self.val = x 
         self.left = left 
         self.right = right
         
         
class tree: 
    def build(self, s): 
         print(s)
         if not s: return None 
         i = j = 0 
         n = len(s)
         while i < n and s[i].isdigit(): 
             i += 1 
         x = s[j:i]
         root = treeNode(x)
         cnt = 1 
         k = i 
         i += 1 
         while i < n and cnt: 
             if s[i] == ')': cnt -= 1 
             if s[i] == "(": cnt += 1 
             i += 1 
         root.left, root.right = self.build(s[k+1:i-1]), self.build(s[i+1:-1])
         
         return root 
t = tree()
s = "4(2(3)(1))(6(5))"
tree1 = t.build(s)
#print(tree1.val, print(tree1.left.val), print(tree1.right.val))
def preOrder(tree):
    return preOrder(tree.left) + [tree.val] + preOrder(tree.right) if tree else [] 
print(preOrder(tree1)) 
