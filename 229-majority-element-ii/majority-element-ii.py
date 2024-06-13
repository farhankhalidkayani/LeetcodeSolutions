class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj=len(nums)//3
        hashtable=Counter(nums)
        res=[]
        for c in hashtable:
            if hashtable[c]>maj:
                res.append(c)
        return res
                