class Solution(object):
    def isValid(self, s):
        stack=[]
        Hash={"}":"{","]":"[",")":"("}

        for c in s:
                if c in Hash:
                    if stack and stack[-1]==Hash[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
        return True if not stack else False
