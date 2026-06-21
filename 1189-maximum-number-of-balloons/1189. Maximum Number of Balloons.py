from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = defaultdict(int)
        word = 'balloon'
        ans = 0
        
        for c in text:
            if c in word:
                letters[c] += 1
        
        if len(letters) != 5:
            return 0
        
        letters['l'] /= 2
        letters['o'] /= 2
        
        return int(min(letters.values()))
            
        
