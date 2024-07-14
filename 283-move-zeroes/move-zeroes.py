class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonZero]=nums[i]
                nonZero+=1
        while nonZero<len(nums):
            nums[nonZero]=0
            nonZero+=1
        
        