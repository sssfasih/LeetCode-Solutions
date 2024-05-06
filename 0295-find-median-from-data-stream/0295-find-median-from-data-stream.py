class MedianFinder:

    def __init__(self):
        self.small , self.large = [] , []
        self.s_len, self.l_len = 0,0
        
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
            self.l_len += 1
        else:
            heapq.heappush(self.small,num*-1)
            self.s_len += 1
            
        # Make the size of each heap adjusted
        if self.l_len > self.s_len + 1 :
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
            self.l_len -= 1
            self.s_len += 1
        if self.s_len > self.l_len + 1 :
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large ,  val)
            self.s_len -= 1
            self.l_len += 1
    def findMedian(self) -> float:
        if self.l_len > self.s_len:
            return self.large[0]
        elif self.s_len > self.l_len:
            return self.small[0] *-1
        else:
            return (self.large[0]+(self.small[0])*-1)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()