class Solution(object):
    def isAnagram(self, s, t):
      
        lsts=list(s)
        lstt=list(t)
        lsts.sort()
        lstt.sort()
        if lsts==lstt:
            return True
        else:
            return False            
        