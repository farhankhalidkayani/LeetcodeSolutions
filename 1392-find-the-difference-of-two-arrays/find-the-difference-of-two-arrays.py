class Solution(object):
    def findDifference(self, nums1, nums2):
        
        result=[[],[]]
        hash1={}
        hash2={}
        for i in nums1:
            hash1[i]=1
        for i in nums2:
            hash2[i]=1
        for c in hash1:
            if c not in hash2:
                result[0].append(c)
        for c in hash2:
            if c not in hash1:
                result[1].append(c)
        return result


        