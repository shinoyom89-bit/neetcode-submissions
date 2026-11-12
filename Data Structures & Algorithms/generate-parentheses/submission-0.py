class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        result=[]
        def bfs(openn,closen):
            if openn==closen==n:
                result.append("".join(stack))
                return
            if openn<n:
                stack.append("(")
                bfs(openn+1,closen)
                stack.pop()
            if closen<openn:
                stack.append(")")
                bfs(openn,closen+1)
                stack.pop()
        bfs(0,0)
        return result