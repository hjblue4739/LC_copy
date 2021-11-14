class treeNode: 
  def __init__(self, val, left = None, right = None, parent = None): 
      self.val = val 
      self.left = left 
      self.right = right
      self.parent = parent

class Solution:
    #
    def lowestCommonAncestor(self, root, p, q):
        def dfs(x): 
            if x in (None, p, q): return x
            l, r = dfs(x.left), dfs(x.right)
            return x if (l and r) else l or r
        return dfs(root)
      
      
    #solution 1 
    # #1) find p first  
    # 2) traverse up (towards ancestors) and use hash set to store the parent node of p
    # #3) find q
    # 4) traverse up in similar way as step 2, if any node already in the hash set, return the node 
    # time complexity O (log N); space O (log N) 
    #solution 2 
    # 1) assume dist(p, LCA) = L1, dist(q, LCA) = L2, dist(root, LCA) = L3 
    # 2)            pointer 1's path: p -> LCA -> root, reset start point at q, q -> LCA (total distance L1 + L3 + L2) 
    #    meanwhile, pointer 2's path: q -> LCA -> root, reset start point at p, p -> LCA (total distance L2 + L3 + L1)
    #.   pointer 1 and 2 would meet at LCA since the total distance they move are the same 
    
    
    
    
    
    
    
    
    
    
    
