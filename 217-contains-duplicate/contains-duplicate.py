class Solution(object):
    def containsDuplicate(self, nums):
         Myset = set()

         for num in nums:
            if num in Myset:
                return True
            
            Myset.add(num)    
         return False