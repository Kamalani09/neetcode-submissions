class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        drops = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                drops += 1
        if n > 1 and nums[0] < nums[-1]:
            drops += 1
        return drops <= 1