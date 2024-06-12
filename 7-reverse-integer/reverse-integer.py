class Solution:
    def reverse(self, x: int) -> int:
        res=0
        isNeg=False
        if x<0:
            isNeg=True
            x=x*-1
        while x>0:
            rem=x%10
            res=(res*10)+rem
            x=x//10
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res if isNeg==False else -res
        