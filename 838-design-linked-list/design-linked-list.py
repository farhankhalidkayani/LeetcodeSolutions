class MyLinkedList:
    
    class ListNode:
        def __init__(self):
            self.val=None
            self.next=None

    def __init__(self):
        self.length=0
        self.head=None
        self.tail=None

        

    def get(self, index: int) -> int:
        if index<0 or index>=self.length:
            return -1
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp.val
        

    def addAtHead(self, val: int) -> None:
        temp= ListNode()
        temp.val=val
        if self.head==None:
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
        self.length+=1
        

    def addAtTail(self, val: int) -> None:
        temp= ListNode()
        temp.val=val
        if self.tail==None:
            self.head=temp
            self.tail=temp
        else:
            self.tail.next=temp
            self.tail=temp
        self.length+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.length: return
        if index==0:
            self.addAtHead(val)
            return
        if index==self.length:
            self.addAtTail(val)
            return
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        newNode= ListNode()
        newNode.val=val
        newNode.next=temp.next
        temp.next=newNode
        self.length+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.length:
            return 
        if index==0:
            self.head=self.head.next
            self.length-=1
            if self.length==0:
                self.tail=None
            return
        
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        temp.next=temp.next.next
        if index==self.length-1:
            self.tail=temp
        self.length-=1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)