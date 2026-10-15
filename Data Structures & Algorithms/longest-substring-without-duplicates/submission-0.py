class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        sett=set()
        max_len=0
        for right in range(len(s)):
            
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            
            w=(right-left)+1
            max_len=max(max_len,w)
            sett.add(s[right])
        return max_len

        