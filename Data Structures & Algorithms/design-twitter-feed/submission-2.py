class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.tweets_posted = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweets_posted, tweetId))
        self.tweets_posted += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets[userId])
        for user in self.follows[userId]:
            feed += self.tweets[user]
        feed = sorted(feed, key=lambda x: x[0],reverse=True)        
        return [tweet for time, tweet in feed[:10]]

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
