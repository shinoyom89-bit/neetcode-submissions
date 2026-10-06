from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash=collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append([value,timestamp]) #[val,time] 0 pe value hai and 1 pe time hai 

    def get(self, key: str, timestamp: int) -> str:
        left=0
        right=len(self.hash[key])-1
        return_val=""
        while left<=right:
            mid=(left+right)//2
            if self.hash[key][mid][1]<=timestamp:
                return_val=self.hash[key][mid][0]
                left=mid+1
            else:
                right=mid-1
        return return_val
