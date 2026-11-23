class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        maj=nums[0]
        for num in nums:
            if maj==num:
                count+=1
            elif count==0:
                maj=num
            else:
                count-=1
        return maj