class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_center(l,r,s):
            cnt = 0
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        cnt = 0
        for i in range(len(s)):
            #odd
            cnt += expand_center(i,i,s)

            #even 
            cnt += expand_center(i,i+1,s)


        return cnt


        