from collections import deque
class MyStack:

    def __init__(self):
        self.queue1=deque()
        self.queue2=deque()
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue1)-1):
            x=self.queue1.popleft()
            self.queue2.append(x)
        for i in range(len(self.queue2)):
            x=self.queue2.popleft()
            self.queue1.append(x)
        return self.queue1.popleft()
        

    def top(self) -> int:
        return self.queue1[-1]
        

    def empty(self) -> bool:
        return len(self.queue1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()