class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        total = 0

        for i in range(len(gain)):
            total += gain[i]
            alt.append(total)
        
        return max(alt)