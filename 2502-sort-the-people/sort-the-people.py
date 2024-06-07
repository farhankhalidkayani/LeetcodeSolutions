class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashtable={}
        res=[]
        for i in range(len(names)):
            hashtable[heights[i]]=names[i]
        for i in range(len(names)):
            res.append(hashtable[max(hashtable)])
            hashtable.pop(max(hashtable))

            
        return res
        
        