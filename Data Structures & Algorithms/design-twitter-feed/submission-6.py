import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.userids = []
        self.followings = dict()
        self.tweets = dict()
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((-self.count, tweetId))
        else:
            self.tweets[userId] = [(-self.count, tweetId)]
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        users_to_check = {userId} | self.followings.get(userId, set())

        for user in users_to_check:
            if user in self.tweets:
                for tweet in self.tweets.get(user):
                    heapq.heappush(min_heap, tweet)
                    # if len(min_heap) > 10:
                    #     heapq.heappop(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(min(10, len(min_heap)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:  # Avoid self-following
            return
        if followerId not in self.followings:
            self.followings[followerId] = set()
        self.followings[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followings:
            self.followings[followerId].discard(followeeId)

