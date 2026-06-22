class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        ans = ''

        for c in s:
            counts[c] = counts.get(c, 0) + 1

        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        for k, v in sorted_counts:
            for i in range(v):
                ans += k

        return ans