class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        cumsum = 0

        for i in range(len(gain)):
            cumsum += gain[i]
            alt.append(cumsum)
        
        return max(alt)