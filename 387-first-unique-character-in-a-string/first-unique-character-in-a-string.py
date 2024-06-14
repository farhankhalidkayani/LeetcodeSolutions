class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable=Counter(s)
        for i,n in enumerate( s):
            if hashtable[n]==1:
                return i
            
        return -1
        