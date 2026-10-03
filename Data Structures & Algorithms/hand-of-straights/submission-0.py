class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnts = Counter(hand)
        hand.sort()
        for n in hand:
            if cnts[n]:
                for i in range(n,n+groupSize):
                    if not cnts[i]:
                        return False
                    cnts[i] -= 1
        return True