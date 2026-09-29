class Solution:
    def encode(self, strs: List[str]) -> str:
        combine=""
        for s in strs:
            combine+=str(len(s))+"#"+s
        return combine
    
    def decode(self,s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s)-1:
            j=i
            while s[j]!="#":
                j+=1
            char_len=int(s[i:j])
            res.append(s[j+1:j+1+char_len])
            i=j+1+char_len
        return res