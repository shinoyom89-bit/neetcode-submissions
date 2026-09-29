class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=count.get(n,0)+1
        arr=[]
        for number,count in count.items():
            arr.append([count,number])
        arr.sort()
        res=[]
        while len(res)!=k:
            res.append(arr.pop()[1])
        return res

