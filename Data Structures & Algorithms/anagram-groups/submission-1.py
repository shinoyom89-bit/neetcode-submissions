class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for c in strs:
            key="".join(sorted(c))
            if key in hash:
                hash[key].append(c)
            else:
                hash[key]=[c]
        return list(hash.values())
        