class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        arr=[(key,value) for key,value in freq.items()]
        arr.sort(reverse=True,key=lambda x:x[1])
        return [x[0] for x in arr[0:k]]