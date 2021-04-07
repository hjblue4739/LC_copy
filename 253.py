class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        result, curr = 0, 0
        for i, val in sorted(x for interval in intervals for x in [(interval[0], 1), (interval[1], -1)]):
            curr += val
            result = max(curr, result)
        return result

# import heapq
#
#
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         if not intervals: return 0
#         q = []
#         for interval in sorted(intervals, key=lambda x: x[0]):
#             if not q:
#                 heapq.heappush(q, interval[1])
#             else:
#                 if interval[0] >= q[0]:
#                     heapq.heappop(q)
#                 heapq.heappush(q, interval[1])
#         return len(q)



##leetcode 253
#Problem Description
#Given an array of meeting time intervals consisting of 
#start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#Example 1:
#Input: [[0, 30],[5, 10],[15, 20]]
#Output: 2
#Example 2:
#Input: [[7,10],[2,4]]
#Output: 1

class meetings: 
    def rooms_needed(self, times):
        traverse_times = list(zip(*times))
        mn, mx = min(traverse_times[0]), max(traverse_times[1])
        d = [0] * (mx - mn + 2)
        for s, e in times:
            d[s - mn] += 1
            d[e - mn] -= 1
        res = d[0]
        for i in range(1, len(d)):
            d[i] += d[i-1]
            res = max(res, d[i])
            print(res)
        return res
    
tmp2 = meetings()
times = [[0, 30],[5, 10],[15, 20],[2,4]]
tmp2.rooms_needed(times)

            

class Solution(object):
    def minMeetingRooms(self, intervals):
        rooms, starts, ends = 0, sorted(i[0] for i in intervals), sorted([i[1] for i in intervals], reverse = 1)
        for s in starts:
            #now a meeting is going to start, is there a meeting ends (i.e., a meeting room is released)?
            if ends[-1] <= s:
                ends.pop()
            else:
                #need to ask for a new room
                rooms += 1
        return rooms

tmp = Solution()
tmp.minMeetingRooms(times)

#Given a list of intervals calendar and a number of available conference rooms. For each query, 
#return true if the meeting can be added to the calendar successfully without causing a conflict, 
#otherwise false. A conference room can only hold one meeting at a time.

Input:
calendar = times = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
rooms = 3
queries = [[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]
Output: [false, true, false, true, false, true, false, false, false, true]


class meetings:  
    def conflict(self, times, rooms, queries):
        traverse_times = list(zip(*times))
        mn, mx = min(traverse_times[0]), max(traverse_times[1])
        d = [0] * (mx - mn + 2)
        c = d[:]
        for s, e in times:
            d[s - mn] += 1
            d[e - mn] -= 1
        
        for i in range(1, len(d)):
            d[i] += d[i-1]
            c[i] = d[i]
        res = []
        for s, e in queries: 
            if s >= mx or e <= mn: 
                res.append(True)
            else: 
                cur = max(c[max(0,s-mn):min(len(d), e-mn)])
                res.append(cur + 1 <= rooms)
        return res
