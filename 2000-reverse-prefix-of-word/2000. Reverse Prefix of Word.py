class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)
        l = 0
        ch_bool = 0

        for r in range(len(arr)):
            if arr[r] == ch and ch_bool == 0:
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                ch_bool = 1

        return ''.join(arr)