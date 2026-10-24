class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_center(l,r,s,cnt):
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        cnt1 = 0
        cnt2 = 0
        cnt = 0
        for i in range(len(s)):
            #odd
            cnt1 += expand_center(i,i,s,cnt)

            #even 
            cnt2 += expand_center(i,i+1,s,cnt)


        return cnt1+cnt2


        