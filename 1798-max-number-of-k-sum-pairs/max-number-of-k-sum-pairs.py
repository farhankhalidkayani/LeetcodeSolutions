class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashtable={}
        count=0
        for num in nums:
            diff=k-num
            if diff in hashtable and hashtable[diff]>0:
                hashtable[diff]-=1
                count+=1
            else:
                if num in hashtable:
                    hashtable[num]+=1
                else:
                    hashtable[num]=1
        return count

        