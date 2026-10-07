class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # maps users to a list of their tweets
        self.follows = defaultdict(set) # maps users to a list of the following
        self.total_tweets = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.total_tweets, tweetId))
        self.total_tweets += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets[userId])
        # print(f"feed (pre) :{feed}")
        # print(f"follows:{self.follows[userId]}")
        for user in self.follows[userId]:
            # print("!")
            feed += self.tweets[user]
        heapq.heapify(feed)
        feed = heapq.nlargest(10, feed)
        print(f"feed (post) :{feed}")

        feed = [tweet for tweet_count, tweet in feed]
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
         if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

