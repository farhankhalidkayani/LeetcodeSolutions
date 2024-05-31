class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        hashtable1={}
        hashtable2={}
        for i,c in enumerate(s):
            if c in hashtable1:
                hashtable1[c]+=i
            else:
                hashtable1[c]=i
        for i,c in enumerate(t):
            if c in hashtable2:
                hashtable2[c]+=i
            else:
                hashtable2[c]=i
        for i in range(len(s)):
            if hashtable1[s[i]]!=hashtable2[t[i]]:
                return False
        return True

        