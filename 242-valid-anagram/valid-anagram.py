class Solution(object):
    def isAnagram(self, s, t):
      
     
        
        if len(s)!=len(t):
            return False
        hashtables={}
        hashtablet={}

        for i in range(len(s)):
            hashtables[s[i]]=1+hashtables.get(s[i],0)
            hashtablet[t[i]]=1+hashtablet.get(t[i],0)
        for val in s:
            if hashtables[val]!=hashtablet.get(val,0):
                return False;        
                        
        return True