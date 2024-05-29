class Solution(object):
    def twoSum(self, numbers, target):
        left,right=0,len(numbers)-1
        answer=[]
        while left<right:
            Sum=numbers[left]+numbers[right]
            if Sum<target:
                left+=1
            if Sum>target:
                right-=1
            if Sum==target:
                answer.append(left+1)
                answer.append(right+1)
                return answer
        return answer
        