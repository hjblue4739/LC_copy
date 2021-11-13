class array:
    def findCommon(self, arr1, arr2, arr3): 
        i, j, k = len(arr1)-1, len(arr2)-1, len(arr3)-1
        #i, j, k = 0, 0, 0 
        res = [] 
        while i or j or k: 
            if arr1[i] == arr2[j] == arr3[k]: 
                res.append(arr1[i])
            max_value = max(arr1[i], arr2[j], arr3[k])
            if i and arr1[i] == max_value: 
                i -= 1 
            if j and arr2[j] == max_value: 
                j -= 1
            if k and arr3[k] == max_value: 
                k -= 1
        if arr1[0] == arr2[0] == arr3[0]: 
            res.append(arr1[0])
        return res 
t = array()
print(t.findCommon([1,2],[0,2,5,6],[-1,2,5,6,8])) 

