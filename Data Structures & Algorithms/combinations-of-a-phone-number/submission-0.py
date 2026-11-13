class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl","6":"mno","7":"pqrs","8":"tuv",
            "9":"wxyz"
        }
        stack=[]
        result=[]
        if not digits:
            return []
        def backtrack(index):
            if index>=len(digits):
                result.append("".join(stack))
                return
            for char in phone_map[digits[index]]:
                stack.append(char)
                backtrack(index+1)
                stack.pop()
        backtrack(0)
        return result