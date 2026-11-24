class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            val=abs(num)
            idx=val-1
            if nums[idx]<0:
                res.append(val)
            else:
                nums[idx]=-nums[idx]
        return res
