class Solution(object):
    def twoSum(self, nums, target):
        Myhash={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in Myhash:
                return (Myhash[diff],i)
            Myhash[n]=i                        
        