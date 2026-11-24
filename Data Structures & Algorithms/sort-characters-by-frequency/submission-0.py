class Solution:
    def frequencySort(self, s: str) -> str:
        frq={}
        for ch in s:
            if ch not in frq:
                frq[ch]=1
            else:
                frq[ch]+=1
        res = sorted(frq.items(), key=lambda x: x[1], reverse=True)
        ans=""
        for ch,f in res:
            while f>0:
                ans+=ch
                f-=1
        return ans
