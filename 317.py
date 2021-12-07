    
'''    
317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
Note: There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
The question requires BFS to solve, classic, generally need queue.
'''

### from building to find empty cell 
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        n_spaces = sum(grid[i][j] == 0 for i in range(m) for j in range(n))
        n_buildings = sum(grid[i][j] == 1 for i in range(m) for j in range(n))
        if n_buildings == 0: return 0 #没房子
        if n_spaces == 0: return -1 #有房子但没地
        
        distance = [[0] * n for _ in range(m)]
        buildings = [[0] * n for _ in range(m)]

        def bfs(x, y):
            visited = set()
            queue = deque([(x, y, 0)])
            while queue:
                x0, y0, d = queue.popleft()
                for x, y in [(x0-1, y0), (x0+1, y0), (x0, y0-1), (x0, y0+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited: 
                        visited.add((x, y))
                        buildings[x][y] += 1 #要记得考虑累加空地能访问的房子数。只有能访问所有房子的空地才有可能是最后的答案
                        distance[x][y] += d + 1
                        queue.append((x, y, d + 1))
                        
            return len(visited) == 0 #当房子被挡住不能被任何空地access

        if any(bfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1): return -1
        
        return min([distance[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0 and buildings[i][j] == n_buildings] or [-1])
