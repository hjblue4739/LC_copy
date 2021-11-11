# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###similar to 270 and 658 658. Find K Closest Elements

class tree: 
    def findKClosest(self, root, target, k): 
        def inorder(x): 
            return inorder(x.left) + [x.val] + inorder(x.right) if x else [] 
        
        seq = inorder(root)
        left, right = 0, len(seq) - 1 
        while left + k - 1 < right:  ### note: k - 1 rather k 
            if abs(target - seq[left]) <= abs(target - seq[right]): 
                right -= 1 
            else: 
                left += 1 
        return seq[left:right + 1] ### note: right + 1
