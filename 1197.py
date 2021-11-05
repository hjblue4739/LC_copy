'''
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

'''
def minKnightMoves(self, x: int, y: int) -> int:
        # 8 directions
        directions = {(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)}
        queue = collections.deque()
        visited = set()
        x,y = abs(x), abs(y)
        if x == 1 and y == 1: return 2
        # (x,y,steps)
        queue=deque([(0,0,0)])
        while queue:
            cur_x,cur_y,steps=queue.popleft()
            if [cur_x,cur_y]==[x,y]: return steps
            
            for dx, dy in directions:
                if 0<=cur_x+dx<=300 and 0<=cur_y+dy<=300 and (cur_x+dx,cur_y+dy) not in visited:
                    visited.add((cur_x+dx,cur_y+dy))
                    queue.append((cur_x+dx,cur_y+dy,steps+1))
