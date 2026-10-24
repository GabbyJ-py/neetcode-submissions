class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_center(l,r,s):
            idxs = (0,0)
            w_len = 0
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                idxs = (l,r)
                w_len = r-l+1
                l -= 1
                r += 1
            return idxs, w_len

        long_idxs = (0,0)
        long_wlen = 0
        for i in range(len(s)):
            #odd
            idxs, w_len = expand_center(i,i,s)
            if w_len > long_wlen:
                long_wlen = w_len
                long_idxs = idxs

            #even
            idxs, w_len = expand_center(i,i+1,s)
            if w_len > long_wlen:
                long_wlen = w_len
                long_idxs = idxs
    
        return s[long_idxs[0] : long_idxs[1]+1]



        