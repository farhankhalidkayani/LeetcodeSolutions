class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        
        while left<=right:
            mid=round((left+right)/2)
            
            if target==nums[mid]:
                return mid
            elif target > nums[mid]:
                left=mid+1
                
                continue
            elif target <nums[mid]:
                right=mid-1
                
                continue
        return -1

        