class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        ans = []
        s_len = 0
        cnts = Counter(s)
        cur_set = set()
        for char in s:
            if char not in cur_set:
                left += cnts[char]
                cur_set.add(char)
            s_len+=1
            left-=1
            if left == 0:
                ans.append(s_len)
                cur_set = set()
                s_len = 0
        return ans
            
