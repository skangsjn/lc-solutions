from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        chars1 = Counter(s1)
        chars2 = defaultdict(int)

        if n > len(s2):
            return False

        for i in range(n):
            chars2[s2[i]] += 1
        
        if chars1 == chars2:
            return True
        
        l = 0
        for r in range(n, len(s2)):
            chars2[s2[r]] += 1
            chars2[s2[l]] -= 1
            if chars2[s2[l]] == 0:
                del chars2[s2[l]]
            l += 1

            # chars2 = Counter(s2[l:r+1])
            if chars1 == chars2:
                return True

        
        
        
        return False
            
        