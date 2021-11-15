#Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        res = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
        return res
    
    
'''
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

requirements: 
1) len of nums ? 

special cases: 
1) when nums == [], lower = 0, upper,  return ["lower-upper"]
2) nums = [0,2,5,8], lower = 0, upper = 10, return ["1", "3->4", "6->7","9->10"]

solutions: 
1) iterate nums, from i = 1, to len(nums) - 1 
2) compare nums[i] and nums[i-1]
  if nums[i] == 1 + nums[i-1], then continue
  else: 
    dif = nums[i] - nums[i-1]
    
    start = nums[i] + 1, end = nums[i-1] - 1 
    if start == end: 
      add "start" to result 
    else add "start -> end" to result 
complexity: time o(n), space o(1) excluding the space used by the result 
    
'''


class Range: 
  def findMissRange(self, arr, lower, upper): 
    a = lower - 1 
    result = [] 
    arr.append(upper + 1)
    for b in arr: 
      if b > a + 1:
        start, end = a + 1, b - 1 
        if start == end: 
          result.append(str(start))
        else: 
          result.append(str(start) + '->' + str(end))
      a = b
    arr.pop() 
    return result 
    
    
    
    

    
