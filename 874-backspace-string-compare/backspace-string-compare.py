class Solution(object):
    def backspaceCompare(self, s, t):
        stacks=[]
        stackt=[]
        for c in s:
            if c=='#' and stacks:
                stacks.pop()
                continue
            if c=='#' and not stacks:
                continue
            stacks.append(c)
        for c in t:
            if c=='#' and stackt:
                stackt.pop()
                continue
            if c=='#' and not stackt:
                continue
            stackt.append(c)


        return stacks==stackt

        