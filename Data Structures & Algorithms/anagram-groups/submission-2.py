class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            sorteds=''.join(sorted(s)) #['a'.'b','c']
            result[sorteds].append(s)
        return list(result.values())
