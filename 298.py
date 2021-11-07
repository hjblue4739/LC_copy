# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###consecutive, and increasing such as [1,2,3]
class Solution:
    def longestConsecutive(self, root):
        if not root: return 0
        result = 0
        stack = [(root, 1)]
        while stack:
            node, curr = stack.pop()
            result = max(result, curr)
            l, r, v = node.left, node.right, node.val
            for x in [l,r]: 
                if x:
                    stack.append((x, curr+1 if x.val == v+1 else 1))
        return result
    
### increasing only [1,5,7]
class Solution:
    def longestConsecutive(self, root):
        if not root: return 0
        result = 0
        stack = [(root, 1)]
        while stack:
            node, curr = stack.pop()
            result = max(result, curr)
            l, r, v = node.left, node.right, node.val
            for x in [l,r]: 
                if x:
                    stack.append((x, curr+1 if x.val > v else 1))
        return result
    
