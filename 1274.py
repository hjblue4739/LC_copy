'''
#There are some ships on the two-dimensional sea level represented by the Cartesian coordinate system. Each ship is on an integer point, and each integer point has at most 1 ship.#Has a functionSea.hasShips(topRight, bottomLeft) , The input parameters are the coordinates of the upper right corner and the lower left corner. This function returns if and only if there is at least one ship in the rectangular area (including the boundary) represented by these two pointstrue , Otherwise returnfalse 。
Give you the upper right corner of the rectangletopRight And the bottom left cornerbottomLeft Please return the number of ships in this rectangle. The title guarantees the rectangleThere are only 10 ships at most。
Call functions hasShips More than 400 times Will be sentenced toWrong Answer . At the same time, any attempt to bypass the evaluation system will be disqualified.
Example:
https://www.programmersought.com/article/59234825199/
'''

class Solution(object):
    def countShips(self, sea: 'Sea', tp: 'Point', lp: 'Point') -> int:
        if lp.x > tp.x or lp.y > tp.y or not sea.hasShips(tp, lp):
            return 0
        if tp.x == lp.x and tp.y == lp.y:
            return 1
        nx, ny = (tp.x + lp.x)//2, (tp.y + lp.y)//2
        return self.countShips(sea, Point(nx, tp.y), Point(lp.x, ny + 1)) +\. ### 
            self.countShips(sea, Point(nx, ny), lp) + \
            self.countShips(sea, tp, Point(nx + 1, ny + 1)) + \
            self.countShips(sea, Point(tp.x, ny), Point(nx + 1, lp.y))
