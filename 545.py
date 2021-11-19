'''
[LeetCode] 545. Boundary of Binary Tree 二叉树的边界
 

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.result = [root.val]
        self.leftBoundary(root.left)
        self.leaves(root.left)
        self.leaves(root.right)
        self.rightBoundary(root.right)
        return self.result

    def leftBoundary(self, node):
        if not node or (not node.left and not node.right): return ##avoid to add leaf node 
        self.result.append(node.val)
        l, r = node.left, node.right
        self.rightBoundary(l or r)

    def rightBoundary(self, node):
        if not node or (not node.left and not node.right): return ###avoid to add leaf node 
        l, r = node.left, node.right
        self.rightBoundary(r or l)
        self.result.append(node.val)

    def leaves(self, node):
        if not node: return
        if not node.left and not node.right:
            self.result.append(node.val)
            return
        self.leaves(node.left)
        self.leaves(node.right)
        
        
        
        
  def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None: return []
        res=[root.val]
        def leftBoundary(root):
            if root is None or root.left is None and root.right is None: return
            res.append(root.val)
            if root.left:
                leftBoundary(root.left)
            else:
                leftBoundary(root.right)
            
        def rightBoundary(root):
            if root is None or root.left is None and root.right is None: return
            if root.right:
                rightBoundary(root.right)
            else:
                rightBoundary(root.left)
            res.append(root.val)
            
        def leaves(node):
            if node is None: return
            if node.left is None and node.right is None and node != root:
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)
        
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return res
    
 
