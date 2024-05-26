class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        unique=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[unique]=nums[i]
                unique+=1 
        return unique        