class Solution(object):
    def findDifference(self, nums1, nums2):
        
        result=[[],[]]
        hash1=set(nums1)
        hash2=set(nums2)
        
        for c in hash1:
            if c not in hash2:
                result[0].append(c)
        for c in hash2:
            if c not in hash1:
                result[1].append(c)
        return result


        