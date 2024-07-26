class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis={')':'(', '}':'{',  ']':'['  }
        stack=[]
        for par in s:
            if par in parenthesis:
                if stack and stack[-1]==parenthesis[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return True if not stack else False
            
        