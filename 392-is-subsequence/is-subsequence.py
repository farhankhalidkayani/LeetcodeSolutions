class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)>len(t):
            return False
        one,sec=0,0
        flag=1
       
        while one<len(s) and sec<len(t):
            if(s[one]==t[sec] ):
                one+=1
                sec+=1
                if(one==len(s)):
                    flag=1
            else:
                sec+=1
                flag=0
        return flag
        