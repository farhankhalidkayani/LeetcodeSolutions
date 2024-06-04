class Solution:
    def average(self, salary: List[int]) -> float:
        Min=min(salary)
        Max=max(salary)
        
        return (sum(salary)-Min-Max)/(len(salary)-2)
        