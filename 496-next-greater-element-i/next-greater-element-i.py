class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hashmap={n:i for i,n in enumerate(nums1)}
        result=[-1]*len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in hashmap:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    index=hashmap[nums2[i]]
                    result[index]=nums2[j]
                    break 
        return result