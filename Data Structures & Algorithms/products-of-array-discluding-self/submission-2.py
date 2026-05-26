class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      prod=1
      zeros_cnt=0
      for x in nums:
            if x!=0:
                  prod*=x
            else:
                zeros_cnt+=1      
      if zeros_cnt>1: return [0]*len(nums)
      res=[]            
      for x in nums:
            if(x!=0 and zeros_cnt>0):
                res.append(0)
            elif x!=0:
                res.append(prod//x)
            else:
                res.append(prod)
      return res   