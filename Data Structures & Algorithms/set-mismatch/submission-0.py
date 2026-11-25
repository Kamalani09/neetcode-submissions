class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f={}
        res=[]
        for num in nums:
            if num not in f:
                f[num]=1
            else:
                f[num]+=1
        for k,v in f.items():
            if v>1:
                res.append(k)
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
           
