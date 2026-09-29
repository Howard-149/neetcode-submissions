class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set) # FollowerID -> Set of followees
        self.msgs = defaultdict(list) # UserID -> tweets
        self.cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.msgs[userId].append((self.cnt,tweetId))
        self.cnt+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follow_map[userId]
        followees.add(userId)
        heap = []
        for followee in followees:
            msgs = self.msgs[followee]
            if len(msgs)>10:
                msgs = msgs[-10:]
            for msg in msgs:
                if len(heap)>=10:
                    heapq.heappushpop(heap,msg)
                else:
                    heapq.heappush(heap,msg)
        ans = []
        for _ in range(len(heap)):
            cnt, tweetId = heapq.heappop(heap)
            ans.append(tweetId)
        return ans[::-1]
            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
