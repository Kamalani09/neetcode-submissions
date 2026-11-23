class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq={}
        for ch in s:
            if ch not in frq:
                frq[ch]=1
            else:
                frq[ch]+=1
        ans=None
        for k,v in frq.items():
            if v==1:
                ans=k
                break
        if ans==None:
            return -1
        for i in range(len(s)):
            if s[i]==ans:
                return i
