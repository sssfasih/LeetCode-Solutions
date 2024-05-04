class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        people.sort()
        count = 0
        while people:
            x = people.pop()
            if people and people[0] + x <= limit:
                people.pop(0)
            count+=1
        return count