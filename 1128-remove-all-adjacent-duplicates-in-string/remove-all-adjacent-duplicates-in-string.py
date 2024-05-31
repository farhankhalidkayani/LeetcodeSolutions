class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        i=0
        while i<len(s):
            
            stack.append(s[i])
            i+=1
            if len(stack)>=2 and stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)
        