class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_list = [0] * 26
        l = 0
        max_len = 0

        for r in range(len(s)):
            char_list[ord(s[r]) - ord("A")] += 1
            while (r-l+1) - max(char_list) > k:
                char_list[ord(s[l])-ord("A")] -= 1
                l += 1
            max_len = max(max_len, r-l+1)

        return max_len

        