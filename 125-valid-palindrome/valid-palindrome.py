class Solution(object):
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        while left<right:
            while not s[left].isalnum() and left<right:
                left+=1
            while not s[right].isalnum() and right>left:
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True