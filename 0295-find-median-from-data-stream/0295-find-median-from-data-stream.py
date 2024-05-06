class MedianFinder:

    def __init__(self):
        self.small , self.large = [] , []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,num*-1)
            
        # Make the size of each heap adjusted
        if len(self.large) > len(self.small) + 1 :
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        if len(self.small) > len(self.large) + 1 :
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large ,  val)
            
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return self.small[0] *-1
        else:
            return (self.large[0]+(self.small[0])*-1)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()