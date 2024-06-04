class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        Max=max(*arr)
        for i in range(len(arr)):
            if arr[i]==Max:
                return i
        
        