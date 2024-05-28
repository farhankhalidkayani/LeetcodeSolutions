class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        actual=n*(n+1)/2
        result=sum(nums)
        return actual-result
        
        