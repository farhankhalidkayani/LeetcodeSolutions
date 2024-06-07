class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashtable={}
        res=[]
        for i in range(len(names)):
            hashtable[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in range(len(names)):
            res.append(hashtable[heights[i]])
        return res
        
        