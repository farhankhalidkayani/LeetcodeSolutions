class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        self.stack.append(val)
        if self.minstack==[]:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))
        

    def pop(self):
       self.stack.pop()
       self.minstack.pop()
        

    def top(self):
       return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()