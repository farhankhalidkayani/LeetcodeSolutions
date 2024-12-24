class BrowserHistory:
    class ListNode:
        def __init__(self,val=None):
            self.val=val
            self.next=None
            self.prev=None

    def __init__(self, homepage: str):
        self.history=self.ListNode(homepage)
        self.curr=self.history
        
        

    def visit(self, url: str) -> None:
        temp=self.curr
        temp.next=self.ListNode(url)
        temp=temp.next
        temp.prev=self.curr
        self.curr=temp
        

    def back(self, steps: int) -> str:
        while self.curr.prev!=None and steps!=0:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while self.curr.next!=None and steps!=0:
            self.curr=self.curr.next
            steps-=1
        return self.curr.val
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)