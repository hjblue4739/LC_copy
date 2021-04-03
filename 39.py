# Time Complexity: O(N^target); O(k * 2^n)
# Space Complexity:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.search(candidates, target, [], result)
        return result

    def search(self, candidates, target, path, result):
        if target == 0:
            result.append(list(path))
            return
        for i in range(len(candidates)):
            if target - candidates[i] < 0: break
            self.search(candidates[i:], target - candidates[i], path + [candidates[i]], result)
            
class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        res = []
        def dfs(i, total, path):
            for j, v in enumerate(c[i:], i):
                if v + total < t: 
                    dfs(j, v + total,  path + [v])
                elif v + total == t: 
                    res.append(path + [v])
            return res
        return dfs(0, 0, [])
    
                
before 0, I need to clarify that my analysis is based on JAVA backtracking implementation

(0) If you can understand Chinese, please see https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/039_Combination_Sum.java directly.

(1) Let us see the difference between Combination Sum and Combination Sum II:
The input of Combination Sum has no dups, but each element can be used for MORE than one time.
The input of Combination Sum II has dups, but each element can be used ONCE.

(2) Let us understand the time complexity of Combination Sum II at the beginning:
O(k * 2 ^ n) is the time complexity of Combination Sum II:
k is average length of each solution, and we need O(k) time to copy new linkedlist when we get one combination.

Solution space:
Since we use one element ONLY for one time, so, for the combinations with k elements, the number of different choices is C(n, k). And most of the time, this number is far smaller than k. But what is the worst case?
int[] arr = {1,1,1,1,1,1,1,1,1}, target is 2, in this case, the number can actually reach C(n,k).

Considering that the combinations may have different length, which range from 0 ~ n. So, there are at most
C(n,0) + C(n,1) + C(n,2) + ... C(n,n) solutions. We know that C(n,0) + C(n,1) + C(n,2) + ... C(n,n) = 2^n. Then we got the time complexity of Combination Sum II which is O(k * 2 ^ n).

(3) Then how we convert Combination Sum to Combination Sum II?
For example, given int[] arr = {2, 3, 4, 5, 6} and target is 10 and each element can be used for MORE than once.
Actually, it is same with the problem: given int[] arr = {2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6}, and target 10, each element can be used for ONLY one time, which is the same description of Combination Sum II.

And you must find that for the new array, each element E, which is smaller than target, will expand to ceil(target/E). Assume the new array has length n', we can get the time complexity which is O(k * 2 ^ n') using the same analysis of Combination Sum II.

(4) Welcome to correct me if I made mistakes and I am happy to see that:)   
            
            
            
   
                    
                    
            
            

                
            
            
    
