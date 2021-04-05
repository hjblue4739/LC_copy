# Time:  O(klog*k) ~= O(k), k is the length of the positions
# Space: O(k) 
#Number of Islands II
#A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#Example:
#Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]. Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
class Solution(object):
    def numIslands2(self, m, n, positions):
        def find(x):
           if d[x] != x:
               d[x] = find(d[x])
           return d[x]

        def union(x, y):
            d[find(x)] = find(y)
  
        res, cnt, d = [], 0, {}
        for p in positions:
            p = tuple(p)
            d[p] = p 
            cnt += 1

            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nb = (p[0] + i, p[1] + j)
                if nb in d:
                    union(p, nb)# Merge different islands, amortised time: O(log*k) ~= O(1)
                    cnt -= 1
            res.append(cnt)

        return res

tmp = Solution()    
tmp.numIslands2(20, 20, [[5,8],[9,7],[5,7],[9,6],[9,5],[5,6],[1,2],[1,3],[1,4],[1,5],[2,5],[14,7]])

tmp.numIslands2(20, 20, [[4,5],[5,4],[5,6],[6,5],[5,5]])







class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[0 for i in range(n)] for j in range(m)]
        roots, result, island = {}, [], 0
        row, col = [-1, 0, 1, 0], [0, 1, 0, -1]
        for position in positions:
            x, y = position[0], position[1]
            if matrix[x][y] == 1:
                result.append(island)
                continue
            roots[x * n + y] = x * n + y
            this_root = x * n + y
            island += 1
            for i in range(4):
                nx, ny = x + row[i], y + col[i]
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 1:
                    nroot = self.find(nx * n + ny, roots)
                    if nroot != this_root:
                        roots[nroot] = this_root
                        island -= 1
            result.append(island)
            matrix[x][y] = 1
        return result

    def find(self, node, roots):
        root = node
        while root != roots[root]:
            root = roots[root]
        while node != root:
            node, roots[node] = roots[node], root
        return root
