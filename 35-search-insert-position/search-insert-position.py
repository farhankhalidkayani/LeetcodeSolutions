class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res="None"
        for i in range(len(nums)):
            if target==nums[i]:
                res=i
            elif target>=nums[i]:
                res=i+1
        if res=="None" and target>max(nums):
            return len(nums)
        elif res=="None" and target<min(nums):
            return 0
        else:
            return res
            

        