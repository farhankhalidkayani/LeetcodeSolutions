class Solution(object):
    def findDuplicate(self, nums):
        hashset=set()
        for c in nums:
            if c in hashset:
                return c
            hashset.add(c)

            
            
            