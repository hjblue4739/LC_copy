[LeetCode] 694. Number of Distinct Islands 不同岛屿的个数
 
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011
Given the above grid map, return 1.

 

Example 2:

11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:

11
1
and

 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.

class solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        shapes = set()
        visited = set()
        def dfs(x, y, pos, island):
            for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] and (nx,ny) not in visited:
                    temp = (pos[0] + dx, pos[1] + dy)
                    visited.add((nx, ny))
                    island.append(temp)
                    dfs(nx, ny, temp, island)
            return tuple(island)
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] and (x,y) not in visited:
                    visited.add((x,y))
                    shapes.add(dfs(x,y,(0,0),[])) ##shapes.add(dfs(x,y,(0,0),[(0,0)]))
        return len(shapes)
    
