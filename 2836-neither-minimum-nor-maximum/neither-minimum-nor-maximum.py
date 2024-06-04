class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        Min=min(nums)
        Max=max(nums)
        for c in nums:
            if Min!=c and c!=Max:
                return c
        return -1        