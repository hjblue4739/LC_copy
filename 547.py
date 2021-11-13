'''
#https://zxi.mytechroad.com/blog/graph/leetcode-547-friend-circles/
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ithand jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Time complexity: O(n^2)
Space complexity: O(n)
Running Time: 162 ms
'''

class Solution(object):
    def findCircleNum(self, M):        
        def dfs(M, curr, n):
            for i in xrange(n):
                if M[curr][i] == 1:
                    M[curr][i] = M[i][curr] = 0
                    dfs(M, i, n)
        
        n = len(M)
        ans = 0
        for i in xrange(n):
            if M[i][i] == 1:
                ans += 1
                dfs(M, i, n)
        
        return ans
    
    

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        roots = list(range(N))
        result = N

        def find(node):
            root = node
            while roots[root] != root:
                root = roots[root]
            while node != root:
                roots[node], node = root, roots[node]
            return root

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                elif M[i][j] == 1:
                    x, y = find(i), find(j)
                    if x == y:
                        continue
                    else:
                        roots[y] = x
                        result -= 1
        return result

    
