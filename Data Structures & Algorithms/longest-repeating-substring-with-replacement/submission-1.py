class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=right=string_len=max_cnt=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_cnt=max(max_cnt,count[s[right]])
            
            while ((right-left)+1)-max_cnt>k:
                count[s[left]]-=1
                left+=1
            window=(right-left)+1
            string_len=max(string_len,window)
        return string_len