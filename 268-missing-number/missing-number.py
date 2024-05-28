class Solution(object):
    def missingNumber(self, nums):
        hashset=set(nums)
        for i in range(len(nums)+1):
            if i not in hashset:
                return i
        
        