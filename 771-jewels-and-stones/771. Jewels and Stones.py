from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set(jewels)
        
        return sum(s in j_set for s in stones)
        