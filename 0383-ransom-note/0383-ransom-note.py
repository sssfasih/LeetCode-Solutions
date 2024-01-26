class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        for i in range(len(magazine)):
            for j in range(len(ransomNote)):
                if ransomNote[j] == magazine[i]:
                    ransomNote.pop(j)
                    break
        if ransomNote:return False
        return True