class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = -1
        for num in nums:
            val = abs(num)
            idx = val - 1
            if nums[idx] < 0:
                duplicate = val
            else:
                nums[idx] = -nums[idx]
        missing = -1
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break
        return [duplicate, missing]