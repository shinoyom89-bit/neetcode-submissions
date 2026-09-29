
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1]<t:
                day_start=stack.pop()[0]
                wait=i-day_start
                res[day_start]=wait
            stack.append([i,t])
        return res