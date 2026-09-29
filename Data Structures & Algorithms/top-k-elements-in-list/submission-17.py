class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            if n not in count:
                count[n]=count.get(n,0)+1
            elif n in count:
                count[n]+=1
        arr=[]
        #2nd pe count hai and 1st pe number
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        res=[]
        while len(res)!=k:
            res.append(arr.pop()[1])
        return res
