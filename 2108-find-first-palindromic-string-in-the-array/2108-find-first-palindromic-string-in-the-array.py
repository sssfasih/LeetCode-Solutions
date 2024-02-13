class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in range(len(words)):
            word_length = len(words[i])
            palindrome = False
            
            #Manual Palindrome Checking ( not using [--1] notation :v )
            for j in range(word_length//2 +1):
                if words[i][j] == words[i][word_length-j-1]:
                    palindrome = True
                else:
                    palindrome = False
                    break
            if palindrome:
                return words[i]
        return ''

