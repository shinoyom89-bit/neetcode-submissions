class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        numss=sorted(nums)
        for index,num1 in enumerate(numss):
            if num1==numss[index-1] and index>0:
                continue
            left=index+1
            right=len(numss)-1
            while left<right:
                total=num1+numss[left]+numss[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    output.append([num1,numss[left],numss[right]])
                    left+=1
                    while left<right and numss[left]==numss[left-1]:
                        left+=1
        return output