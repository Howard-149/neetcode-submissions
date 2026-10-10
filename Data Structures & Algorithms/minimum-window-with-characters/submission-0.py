class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        ans, anslen = [], float("inf")
        l =0

        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r-l+1 < anslen:
                    ans = [l,r]
                    anslen = r-l+1
                c = s[l]
                window[c] -= 1
                l+=1
                if window[c] < countT[c]:
                    have -= 1 
        if not ans:
            return ""            
        return s[ans[0]:ans[1]+1]
