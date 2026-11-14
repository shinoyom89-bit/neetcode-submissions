class Solution:
    def partition(self, s: str) -> List[List[str]]:
        current,result=[],[]
        def dfs(i):
            if i>=len(s):
                result.append(current.copy())
                return  
            for ii in range(i,len(s)):
                var=s[i:ii+1]
                if var==var[::-1]:
                    current.append(var)
                    dfs(ii+1)
                    current.pop()
        dfs(0)
        return result 