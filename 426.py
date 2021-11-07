
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
n1 = Node(1)
n3 = Node(3)
n2 = Node(2, n1, n3)
n5 =Node(5)
n6 =Node(6, n5)
n4 = Node(4, n2, n6)
#root = Node(4, Node(2), Node(6))

class Solution:
    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        if not root: return root
        dummy = head = Node(0)
        stack, curr, prev = [], root, dummy
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            prev.right, top.left, prev = top, prev, top
            curr = top.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
    
    def treeToDoublyList(self, root: 'Node') -> 'Node': 
        #inorder 
        # time complexity O(N)
        # space compexity O(1), average O(logN) if consider the stack used in the recursion
    
        self.tail = dummy = Node(0)
        def traverse(x): 
            if not x: return 
            l, r = x.left, x.right
            traverse(l)
            x.left = self.tail
            self.tail.right = x 
            self.tail = x 
            traverse(r)
        traverse(root)    
        head = dummy.right 
        head.left = self.tail 
        self.tail.right = head 
        return head 

t = Solution()
#new = t.treeToDoublyList(n4)
new = t.treeToDoublyList1(n4)

L = R = new 
for _ in range(10):
    print(L.val, R.val)
    R= R.right
    L =L.left
    
  
