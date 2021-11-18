import collections
import bisect
class string: 
  def ShortestWay(self, source, target): 
    pos = collections.defaultdict(list)
    for i, v in enumerate(source): 
        pos[v].append(i)
    n = len(target)
    furthest = 0 
    result = 0 
    for i, letter in enumerate(target):
        if letter not in pos: return -1 
        if furthest > i: continue
        furthest += 1 
        pre = pos[letter][0]
        while furthest < n: 
            letter2 = target[furthest] 
            if pos[letter2][-1] > pre: 
                idx = bisect.bisect(pos[letter2], pre)
                pre = pos[letter2][idx]
            else: 
                break 
            furthest += 1 
        result += 1 
      
    return result 
t = string()
print(t.ShortestWay('acder', 'aderacderddee'))
print(t.ShortestWay(source = "xyazb", target = "xaabzyaxz"))
