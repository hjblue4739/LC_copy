#Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

#If two nodes are in the same row and column, the order should be from left to right.
'''
Input: 
[3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        d = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new_queue = []
            for node, x in queue:
                d[x].append(node.val)
                if node.left: new_queue.append((node.left, x-1))
                if node.right: new_queue.append((node.right, x+1))
            queue = new_queue
        return [d[k] for k in sorted(d)]
