class Solution:
    def robotWithString(self, s: str) -> str:
        freq = [0] * 26
        t = []
        p = []

        def find_smallest():
            for i in range(len(freq)):
                if freq[i] > 0:
                    return i
            return 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for c in s:
            freq[ord(c) - ord('a')] -= 1
            t.append(c)
            while t and (ord(t[-1]) - ord('a')) <= find_smallest():
                p.append(t.pop())

        # while t:
        #     p.append(t.pop())
        
        return ''.join(p)
        