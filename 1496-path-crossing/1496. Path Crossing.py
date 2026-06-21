from collections import defaultdict

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = defaultdict(int)
        coords[(0, 0)] = 1   
        x = y = 0     

        for c in path:
            if c == 'N':
                y += 1
            if c == 'S':
                y -= 1
            if c == 'E':
                x += 1
            if c == 'W':
                x -= 1
            
            coords[(x, y)] += 1
        
        return len(set(coords.values())) > 1