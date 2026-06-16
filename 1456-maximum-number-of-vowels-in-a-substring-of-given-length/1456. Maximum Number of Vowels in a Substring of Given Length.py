class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for r in range(k):
            if s[r] in vowels:
                count += 1
            ans = max(ans, count)

        for r in range(k, len(s)):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            l += 1

            ans = max(ans, count)

        return ans