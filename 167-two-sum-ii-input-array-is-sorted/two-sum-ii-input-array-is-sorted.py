class Solution(object):
    def twoSum(self, numbers, target):
        left,right=0,len(numbers)-1
        
        while left<right:
            Sum=numbers[left]+numbers[right]
            if Sum<target:
                left+=1
            if Sum>target:
                right-=1
            if Sum==target:
                return[left+1,right+1]
                
       
        