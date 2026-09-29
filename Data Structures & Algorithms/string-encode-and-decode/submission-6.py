class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+=str(len(s))+"#"+s
        return result

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            j=i
            while j<len(s) and s[j]!="#":
                j+=1
            length=int(s[i:j]) # 3#cat j=1 j+1 c
            res.append(s[j+1:length+j+1])
            i=length+j+1
        return res
