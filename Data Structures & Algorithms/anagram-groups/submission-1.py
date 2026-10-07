class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            cnts = [0]*26
            for c in s:
                index = ord(c)-ord('a')
                cnts[index]+=1
            groups[tuple(cnts)].append(s)
        return list(groups.values())