class MyQueue:
    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> int:
        temp = []
        for i in range(1,len(self.lst)):
            temp.append(self.lst.pop())
        x = self.lst.pop()
        for i in range(0,len(temp)):
            self.lst.append(temp.pop())
        return x
    
    def peek(self) -> int:
        return self.lst[0]
        
    def empty(self) -> bool:
        if self.lst:
            return False
        return True
