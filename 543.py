# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0

        def getDiameter(node):
            if not node: return 0
            left = getDiameter(node.left)
            right = getDiameter(node.right)
            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        getDiameter(root)
        return self.result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0 
        if not root: return 0
        def dfs(x): 
            if not x: return 0 
            l, r = dfs(x.left), dfs(x.right)
            self.res = max(self.res, l + r + 1)
            return max(l, r) + 1 
        dfs(root)
        return self.res - 1 
    
    self.res = 0 
    def diameterOfBinaryTree(self, x: TreeNode) -> int:    
        if not x: return 0
        l, r = self.diameterOfBinaryTree(x.left), self.diameterOfBinaryTree(x.right)
        self.res = max(self.res, l + r + 1)
        return max(l, r) + 1 
    
        return self.res - 1 
    
############################if the tree is in another form 
g = [[1,2],[0,3,4],[0,5,6],[1,7],[1,8],[2],[2],[3,9],[4,10],[7,11],[8,12],[9],[10]]

final = [0]
def dfs(node, pre):
    res = [0, 0]
    for nb in g[node]: 
        if nb == pre: continue 
        tmp = dfs(nb, node)
        res.append(tmp)
    res.sort(reverse = 1)
    print(node, res)
    final[0] = max(final[0], sum(res[:2]) +  1)
    return max(res) + 1 
dfs(12, -1)
print(final[0] - 1)


    def diameter(self, x: TreeNode) -> int:    
        if not x: return 0
        cur = [self.d(c) for c in x.chilren] + [0]
        longest2 = nlargest(2,cur)
        self.res = max(self.res, sum(longest2) + 1)
        return max(longest2) + 1 
        return self.res - 1 
    
