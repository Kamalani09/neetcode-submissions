class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for ch in magazine:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
        for ch in ransomNote:
            if ch not in d or d[ch]==0:
                return False
            d[ch]-=1
        return True