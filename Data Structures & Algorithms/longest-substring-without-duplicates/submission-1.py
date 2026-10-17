class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_lenght=0
        sett=set()
        left=0
        right=0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            w=(right-left)+1
            substring_lenght=max(substring_lenght,w)
            sett.add(s[right])
        return substring_lenght