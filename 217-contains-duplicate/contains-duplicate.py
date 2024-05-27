class Solution(object):
    def containsDuplicate(self, nums):
        countMap={}

        for num in nums:
            if num not in countMap:
                countMap[num]=1
            else:
                countMap[num]+=1
                return True
        return False
        