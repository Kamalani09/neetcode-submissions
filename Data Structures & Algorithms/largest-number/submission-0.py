class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a=[]
        for num in nums:
            a.append(str(num))
        n=len(a)
        for i in range(n):
            for j in range(n-i-1):
                if a[j]+a[j+1] < a[j+1]+a[j]:
                    a[j],a[j+1]=a[j+1],a[j]
        if a[0]=="0":
            return "0"
        return "".join(a)