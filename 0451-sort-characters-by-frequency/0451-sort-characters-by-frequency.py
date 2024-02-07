class Solution:
    def frequencySort(self, s: str) -> str:
        #for each char as key, frequency as value 
        hashtable= dict()
        for i in range(len(s)):
            if s[i] in hashtable:
                hashtable[s[i]] += 1
            else:
                hashtable[s[i]] = 1
                
        lst = list(hashtable.items())
        
        # Selection Sort
        for i,data in enumerate(lst):
            key=data[0]
            value= data[1]
            max_idx = i
            for j in range(i+1,len(lst)):
                if lst[j][1] > lst[max_idx][1]:
                    max_idx =j
                    
            lst[i],lst[max_idx] = lst[max_idx],lst[i]
        
        # Return the list in required format (String with char*freq)
        return ''.join( [x[0]*x[1] for x in lst] )
        