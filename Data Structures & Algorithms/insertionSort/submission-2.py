class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
       n=len(pairs)
       res=[]
       for i in range(n):
            j=i-1
        # example of the list --[4,3,2]
            while j>=0 and pairs[j].key > pairs[j+1].key:
                pairs[j],pairs[j+1]=pairs[j+1],pairs[j]
                j-=1
            res.append(list(pairs))
       return res