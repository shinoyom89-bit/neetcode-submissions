from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        s1_window = Counter(s1)
        
        # Check all possible windows of size len1 in s2
        for i in range(len2 - len1 + 1):
            # Use the correct dynamic window size (len1) instead of +2
            current_window = Counter(s2[i : i + len1])
            if current_window == s1_window:
                return True
                
        return False