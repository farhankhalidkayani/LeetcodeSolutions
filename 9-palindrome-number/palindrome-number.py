class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        res=x[::-1]
        return x==res
        