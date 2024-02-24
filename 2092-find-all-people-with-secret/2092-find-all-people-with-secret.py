class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # initialize minheap to get lowest meeting time first
        minheap = []
        # initialize Secret hashtable to mantain who has secret
        secret = {i:False for i in range(n)}
        # 0 has secret and firstPerson has secret on time 0
        secret[0],secret[firstPerson] = True,True
        #meeting is hashtable that mantains list of meetings occured at any instance
        meeting = {}
        # populating hashtable meeting
        for i in range(len(meetings)):
            if meetings[i][2] not in meeting:
                heappush(minheap, meetings[i][2])
                meeting[meetings[i][2]] = [meetings[i][0:2]]
            else:
                meeting[meetings[i][2]].append(meetings[i][0:2])
        
        # for each time stamp, get current meetings list
        while minheap:
            curr_meetings = meeting[heappop(minheap)]
            change = False
            first_run = True
            # if first run, iterate over list, if any new person knows secret, reiterate the list.
            while first_run or change:
                change= False
                first_run = False
                for i in range(len(curr_meetings)):
                    if secret[curr_meetings[i][0]] and secret[curr_meetings[i][1]]:
                        pass
                    elif secret[curr_meetings[i][0]]:
                        secret[curr_meetings[i][1]] = True
                        change= True
                    elif secret[curr_meetings[i][1]]:
                        secret[curr_meetings[i][0]] = True
                        change = True
                        
        # include each person in returning array who knows the truth 
        return [i for i in range(n) if secret[i]==True]