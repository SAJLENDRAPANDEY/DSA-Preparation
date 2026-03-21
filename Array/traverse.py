def missingNum(arr):
        # code here
        arr.sort()
        res=[]
        for i in range(0,len(arr)):
            if arr[i]!=i:
                res.append(i)
        return res
            
arr= [1, 2, 3, 5]
print(missingNum(arr))
