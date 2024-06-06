class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable= {}
        for i in nums:
            if i in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1
        c=0
        m=0
        for n in hashtable:
            if hashtable[n]>c:
                c=hashtable[n]
                m=n
        return m
        