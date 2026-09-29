class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        include=["+","-","*","/"]
        for t in tokens:
            if t not in include:
                stack.append(int(t))
            else:
                a=stack.pop()
                b=stack.pop()
                if t=="+":
                    stack.append(b+a)
                elif t=="-":
                    stack.append(b-a)
                elif t=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return int(stack[0])
      