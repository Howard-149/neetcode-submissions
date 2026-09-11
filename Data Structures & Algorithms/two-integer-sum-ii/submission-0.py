class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(numbers):
            if seen.get(target-n,0):
                return [seen[target-n],i+1]
            seen[n] = i+1


