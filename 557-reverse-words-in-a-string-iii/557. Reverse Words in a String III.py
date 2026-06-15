class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        ans = []

        for i in range(len(arr)):
            word = arr[i]
            end = len(word) - 1
            while end >= 0:
                ans.append(word[end])
                end -= 1
            if i != len(arr) - 1:
                ans.append(' ')

        return ''.join(ans)