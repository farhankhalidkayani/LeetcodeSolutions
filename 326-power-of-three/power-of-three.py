class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n<=0:
            return False
        if n>1 and n%3==0:
            n=n/3
            return self.isPowerOfThree(n)
        if n==1:
            return True
        return False
            
        
        