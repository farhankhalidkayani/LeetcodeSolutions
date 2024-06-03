class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result=[]
        for i in range(len(heights)):
            result.append(heights[i])
        result.sort()
        count=0
        for i in range(len(result)):
            if result[i]!=heights[i]:
                count+=1
        return count
        