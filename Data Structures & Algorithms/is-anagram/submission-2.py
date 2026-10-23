class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for char in s:
            i = ord(char) - ord('a')
            freq[i] += 1

        for char in t:
            i = ord(char) - ord('a')
            freq[i] -= 1

        for count in freq:
            if count != 0:
                return False

        return True