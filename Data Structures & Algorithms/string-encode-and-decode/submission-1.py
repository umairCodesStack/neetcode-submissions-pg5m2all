class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for a in strs:
            for x in a:
               res+=chr(ord(x)+3)   
            res+=" "        
        return res
    def decode(self, s: str) -> List[str]:
            res=[]
            temp=""
            for x in s:
                
                if(x==" "):    
                    res.append(temp)
                    temp=""
                else:
                    temp+=chr(ord(x)-3)      
            return res
