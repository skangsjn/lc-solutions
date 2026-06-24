from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False
        
        chars1 = Counter(s1)
        need = len(chars1)
        
        for i in range(n):
            letter = s2[i]
            if letter in chars1:
                chars1[letter] -= 1
                if chars1[letter] == 0:
                    need -= 1
        
        if need == 0:
            return True
        
        l = 0
        for r in range(n, len(s2)):
            left = s2[l]
            if left in chars1:
                if chars1[left] == 0:
                    need += 1
                chars1[left] += 1
            l += 1

            right = s2[r]
            if right in chars1:
                chars1[right] -= 1
                if chars1[right] == 0:
                    need -= 1

            if need == 0:
                return True

        return False