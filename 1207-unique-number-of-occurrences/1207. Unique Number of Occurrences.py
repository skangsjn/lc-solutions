from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        n_occur = set(freq.values())

        return len(n_occur) == len(freq)