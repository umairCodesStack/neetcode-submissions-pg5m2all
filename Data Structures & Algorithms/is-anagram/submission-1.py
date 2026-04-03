class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1=[x for x in s]
        arr2=[x for x in t]
        if (len(arr1)!=len(arr2)):
            return False
        arr1.sort()
        arr2.sort()
        if (arr1==arr2):
            return True
        return False    
        