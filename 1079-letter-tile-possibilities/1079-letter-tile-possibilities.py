class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        total = 0
        for i in range(1,len(tiles)+1):
            total += len(set(permutations(tiles,i)))
        return total