class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        uniqs=getUniques(arr)
        NumWithfreqs=[]
        for x in uniqs:
            temp=[]
            temp.append(x)
            temp.append(arr.count(x))
            NumWithfreqs.append(temp)
        NumWithfreqs.sort(key=lambda x: x[1], reverse=True)
        print(NumWithfreqs)
        ans=[x[0] for x in NumWithfreqs[0:k]]
        return ans
def getUniques(arr):
    uniqs=[arr[0]]
    for i in range(1,len(arr)):
        temp=arr[0:i]
        if(arr[i] not in temp):
            uniqs.append(arr[i])
    return uniqs        