class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        for i in range(length):
            if (nums[i] in nums[i+1:length]):
                return True
        return False    