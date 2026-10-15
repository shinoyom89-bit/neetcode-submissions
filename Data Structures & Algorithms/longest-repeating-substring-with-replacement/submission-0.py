class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        right=0
        res=0
        max_cnt=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_cnt=max(max_cnt,count[s[right]])

            while ((right-left)+1)-max_cnt>k:
                count[s[left]]-=1
                left+=1 # shrink the window if we cant replace the k char 
            
            res=max(res,right-left+1)
        return res
