'''
548. Split Array with Equal Sum (Medium)
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Example:

Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:

# 1 <= n <=  2000
Elements in the given array will be in range [-10**6, 10**6].
'''
import bisect 
import collections 

class Array: 
    def findSplit(self, nums): 
        n = len(nums)
        if n < 7: return False 
        d = collections.defaultdict(list)
        D = collections.defaultdict(list)
        cum = [0] 
        L = R = 0  
        for i, v in enumerate(nums): 
            cum.append(v + cum[-1])
            D[v].append(i)    

        for i in range(n-4): 
            L += nums[i]
            d[L].append(i+1)
        for k in range(5, n)[::-1]: 
            R += nums[k]
            if R in d: 
                for i in d[R]: 
                    if i + 3 < k: 
                        target = cum[k-1] - cum[i+1] - 2 * R 
                        if target in D:
                            #if any (i+1< j < k-1 for j in D[target]): return True 
                            if bisect.bisect(D[target], i + 1) < bisect.bisect(D[target], k-1): return True 
        return False 
t = Array()
print(t.findSplit([1,2,1,2,1,2,1]))
        
                
        
        
        
        
        
        
