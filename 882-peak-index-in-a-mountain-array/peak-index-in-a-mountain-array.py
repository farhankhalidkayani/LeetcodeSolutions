class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        Max=max(*arr)
        for i,n in enumerate(arr):
            if n==Max:
                return i
        
        