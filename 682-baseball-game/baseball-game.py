class Solution(object):
    def calPoints(self, operations):
        stack=[]
        result=0
        for op in operations:
            if op=="C":
                stack.pop()
            elif op=="D":
                stack.append(stack[-1]*2)
            elif op=="+":
                a=stack[-1]
                stack.pop()
                b=stack[-1]
                stack.append(a)
                stack.append(a+b)                    
            else:
                stack.append(int(op))
        for i in range(len(stack)):
            result+=stack[-1]
            stack.pop()
        return result