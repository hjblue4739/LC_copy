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
