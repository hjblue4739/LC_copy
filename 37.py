class Solution:
    def solveSudoku(self, board):
        from collections import defaultdict as d
        rows, cols, triples, tofill = d(set), d(set), d(set), []
        for r in range(9):
            for c in range(9):
                x, t = board[r][c], (r // 3, c // 3)
                if x != ".":
                    rows[r].add(x)
                    cols[c].add(x)
                    triples[(r // 3, c // 3)].add(x)
                else:
                    tofill.append((r, c, t))
        def dfs():
            #print(board[-1])
            if not tofill:
                return True
            r, c, t = tofill[-1]
            for dig in "123456789": 
                if dig not in rows[r] | cols[c] | triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    tofill.pop()
                    if dfs(): return True
                    board[r][c] = "."
                    rows[r].discard(dig)
                    cols[c].discard(dig)
                    triples[t].discard(dig)
                    tofill.append((r,c,t))
            return False
        dfs()
        

###original
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def findEmpty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def solve(self, board):
        pos = self.findEmpty(board)
        if not pos:
            return True
        x, y = pos[0], pos[1]
        for v in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.isValid(board, x, y, v):
                board[x][y] = v
                if self.solve(board):
                    return True
                board[x][y] = '.'
        return False

    def isValid(self, board, row, col, val):
        for i in board[row]:
            if i == val:
                return False
        bb = list(zip(*board))
        for i in bb[col]:
            if i == val:
                return False

        r, c = row - row % 3, col - col % 3
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] == val:
                    return False
        return True
