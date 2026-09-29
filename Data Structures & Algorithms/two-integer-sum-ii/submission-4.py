class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left < right:
            w_sum=numbers[left]+numbers[right]
            if w_sum> target:
                right-=1
            elif w_sum<target:
                left+=1
            else:
                return [left+1,right+1]