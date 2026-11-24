class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ss1=s1.split(" ")
        ss2=s2.split(" ")
        ss1.extend(ss2)
        f={}
        res=[]
        for word in ss1:
            if word not in f:
                f[word]=1
            else:
                f[word]+=1
        for k,v in f.items():
            if v==1:
                res.append(k)
        return res