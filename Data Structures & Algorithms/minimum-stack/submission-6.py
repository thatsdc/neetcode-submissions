class StackItem: 
    val: int
    next: "StackItem" | None

    def __init__(self, val, next):
        self.val = val
        self.next = next

class MinStack:
    head: StackItem | None = None
    min_item: StackItem | None = None

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        if not self.min_item or self.min_item.val >= val:
            new_min = StackItem(val, self.min_item)
            self.min_item = new_min 

        item = StackItem(val, self.head)
        self.head = item

    def pop(self) -> None:
        print(self.min_item, self.head)
        if self.min_item.val == self.head.val:
            self.min_item = self.min_item.next

        self.head = self.head.next
        
    def top(self) -> int:
        return self.head.val        

    def getMin(self) -> int:        
        return self.min_item.val
        
