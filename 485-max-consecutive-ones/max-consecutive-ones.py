class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=0
        for num in nums:
            if num==1:
                count+=1
                res=max(res,count)
            else:
                res=max(res,count)
                count=0
        return res
        