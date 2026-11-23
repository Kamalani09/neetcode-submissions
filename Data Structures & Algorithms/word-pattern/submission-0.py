class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        d1={}
        d2={}
        for i,j in zip(pattern,words):
            if i in d1 and d1[i]!=j:
                return False
            if j in d2 and d2[j]!=i:
                return False
            d1[i]=j
            d2[j]=i
        return True