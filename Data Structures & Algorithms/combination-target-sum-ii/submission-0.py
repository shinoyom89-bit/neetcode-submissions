class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        candidates.sort()
        result, current = [], []
        def dfs(i, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return
            current.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            current.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return result