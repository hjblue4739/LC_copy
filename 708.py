"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal, head)
        if not head:
            node.next = node
            return node

        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                break
            elif prev.val > curr.val and (insertVal > prev.val or insertVal < curr.val):
                break
            prev, curr = prev.next, curr.next
            if prev == head:
                break
        prev.next = node
        node.next = curr
        return head
    
    
    

# Online Python - IDE, Editor, Compiler, Interpreter



class Node: 
    def __init__(self, val, next = None): 
        self.val = val
        self.next = next 
    
# 4 - > 5 - > 9 -> 1 
head = Node(4)
tmp = head 
for i in [5, 9, 1]: 
    tmp.next = Node(i)
    tmp = tmp.next 
tmp.next = head 
tmp = head 
#for i in range(5): 
#    print(tmp.val)
#    tmp = tmp.next 

print('##########################', head)
def insert(head, target): 
    if not head: return Node(target)
    cur, nxt = head, head.next 
    new = Node(target)
    while True:
        #if cur.val == target: 
        if cur.val <= target <= nxt.val or target > cur.val > nxt.val: cur.next, new.next = new, nxt; return
        cur, nxt = nxt, nxt.next

    
insert(head, 3)
insert(head, 12)
insert(head, 6)
insert(head, 6)
insert(head, 5)
insert(head, 8)
tmp = head 
for i in range(12): 
    print(tmp.val)
    tmp = tmp.next 

    
        
        
