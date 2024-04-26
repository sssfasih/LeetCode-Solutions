class Solution:
    def average(self, salary: List[int]) -> float:
        maxx= 0
        minn = 9999999
        total = 0
        for i in range(len(salary)):
            if salary[i]<minn:
                minn = salary[i]
            if salary[i]>maxx:
                maxx= salary[i]
            total += salary[i]

        return (total-minn-maxx)/(i-1)
                
        
        