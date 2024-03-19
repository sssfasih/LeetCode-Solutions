class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        detector = ''
        for i in range(len(word)):
            if word[i] in '1234567890':
                detector += word[i]
            elif detector:
                nums.add(int(detector))
                detector = ''
        if detector:
            nums.add(int(detector))
        
        return len(nums)
        