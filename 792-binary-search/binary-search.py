class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        mid=round((left+right)/2)
        while left<=right:
            
            
            if target==nums[mid]:
                return mid
            elif target > nums[mid]:
                left=mid+1
                mid=round((left+right)/2)
                continue
            elif target <nums[mid]:
                right=mid-1
                mid=round((left+right)/2)
                continue
        return -1

        