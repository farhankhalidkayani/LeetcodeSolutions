class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hashset=set(nums1)
        res=float("inf")
        for num in nums2:
            if num in hashset:
                res=min(res,num)
        return -1 if res==float("inf") else res

        