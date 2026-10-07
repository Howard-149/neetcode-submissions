class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        ans = []
        for n,cnt in cnts.most_common(k):
            ans.append(n)
        return ans