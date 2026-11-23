class Solution:
    def longestPalindrome(self, s: str) -> int:
        frq={}
        for ch in s:
            if ch not in frq:
                frq[ch]=1
            else:
                frq[ch]+=1
        res=0
        odd=False
        for num in frq.values():
            if num%2==0:
                res+=num
            else:
                odd=True
                res+=num-1
        if odd==True:
            res+=1
        return res