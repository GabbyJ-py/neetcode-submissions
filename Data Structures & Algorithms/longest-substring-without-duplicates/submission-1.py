class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()        
        l = 0
        r = 0
        max_len = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r-l+1)

            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
   
            r += 1

        return max_len

