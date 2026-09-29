class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for c in strs:
            key="".join(sorted(c))
            if key not in hash:
                hash[key]=[c]
            else:
                hash[key].append(c)
        return list(hash.values())
                
        