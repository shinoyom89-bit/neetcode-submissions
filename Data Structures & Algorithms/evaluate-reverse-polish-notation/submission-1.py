class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        include=["+","-","*","/"]
        for number in tokens:
            if number not in include:
                stack.append(int(number))
            else:
                b=stack.pop()
                a=stack.pop()
                if number=="+":
                    stack.append(a+b)
                elif number=="-":
                    stack.append(a-b)
                elif number=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0]

      