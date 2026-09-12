class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = [0] * 26
        s2_cnt = [0] * 26
        N = len(s1)
        for s in s1:
            index = ord(s) - ord('a')
            s1_cnt[index]+=1
        for i in range(N-1):
            s = s2[i]
            index = ord(s) - ord('a')
            s2_cnt[index]+=1
        l = 0
        for r in range(N-1,len(s2)):
            s = s2[r]
            index = ord(s) - ord('a')
            s2_cnt[index]+=1
            if s2_cnt == s1_cnt:
                return True
            else:
                s = s2[l]
                index = ord(s) - ord('a')
                s2_cnt[index]-=1
                l+=1
        return False
                

        