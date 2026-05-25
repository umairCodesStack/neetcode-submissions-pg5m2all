class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        length=len(nums)
        for i in range(length):
            temp=1
            for y in range(length):
                if y!=i:
                    temp*=nums[y]
            res.append(temp)
        return res    