"""
https://leetcode.com/problems/design-twitter/
Concept: 
1) The goal is to create a structure like below which acts as a DB, where we keep track of 
followers, following, and tweets in a set()
- this happens as users post tweets, follow, etc

2) Whenever we post a tweet, track both the tweet id and a timestamp (which is just an increasing counter value in this case)
in a tuple
3) Note that followers and following are considered user ids, so we can use them to query our structure

followee = person that you are following
follower = person that is following

4) Whenever a user follows someone, you need to add to two lists, add the follower to the "following" list for one user,
and then add the followee to the "followed" list of the other user
5) Whenever a user unfollows someone, you remove the follower from the "followed" list, and you also remove the followee from the "following" list

6) Whenever we request a news feed, 
takes the tweet lists from all the users in the "following",
as well as all of the requested user's own tweets. Sort in reverse and take the top 10

getNewsFeed is the most expensive operation here, 
O(N) to retrieve all the tweets of the users in the "following" list (probably more due to the conversion
from set to list)
O(NLogN) to sort them

Alternatively you can use a heap to store the news feed elements, adding only up to 10:
https://www.youtube.com/watch?v=pNichitDD2E&ab_channel=NeetCode

{
    user id 1: {
        followers: set(),
        following: set(),
        feed: [],
        tweets: set()
    },
    user id 2: {
        ...
    },
    ...
}

"""
import heapq

class Twitter:
    def __init__(self):
        """
        Revisited 1/8/2026 with the same solution
        
        user id : {
            followers: [],
            following: [],
            tweets: [],
        }
        """
        self.timestamp = 0
        self.db = {
            
        }

    def postTweet(self, userId: int, tweetId: int) -> None:
        if (userId not in self.db):
            self.db[userId] = {"tweets": [], "followers": set(), "following": set()}
        self.db[userId]["tweets"].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        brute force:
        get the feeds of the followers and also the user's own tweets
        sort them and take the top 10

        slightly more space optimized using a min heap
        start appending tweets into the min heap
        once you reach 10 tweets, if you add another tweet, then
        pop off the top since that's the oldest tweet

        once you get the final list, just reverse by the timestamp,
        and return it so that's in
        ordered from most recent to least recent
        """
        if userId not in self.db:
            self.db[userId] = {"tweets": [], "followers": set(), "following": set()}
        minHeap = []
        for followerId in self.db[userId]["following"]:
            if followerId in self.db:
                # we start iterating from the back to get the oldest tweets
                for i in range(len(self.db[followerId]["tweets"])-1,-1,-1):
                    tweet = self.db[followerId]["tweets"][i]
                    heapq.heappush(minHeap, tweet)
                # if exceeds 10, pop off the top since that's the oldest tweet
                # since we're in a min heap, so the smaller timestamp value = oldest
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        # start iterating from the back to get the oldest tweets
        for i in range(len(self.db[userId]["tweets"])-1,-1,-1):
            tweet = self.db[userId]["tweets"][i]
            heapq.heappush(minHeap, tweet)
            if len(minHeap) > 10:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            timestamp, tweetId = heapq.heappop(minHeap)
            res = [tweetId] + res
        return res
        # brute force: combined + sorting
        # followerTweets = []
        # for followerId in self.db[userId]["following"]:
        #     if followerId in self.db:
        #         followerTweets.extend(self.db[followerId]["tweets"])
        # userTweets = self.db[userId]["tweets"]
        # allTweets = followerTweets + userTweets
        # allTweets.sort(key=lambda x: -x[0])
        # return [tweetId for timestamp, tweetId in allTweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.db:
            self.db[followerId] = {"tweets": [], "followers": set(), "following": set()}
        if followeeId not in self.db:
            self.db[followeeId] = {"tweets": [], "followers": set(), "following": set()}
        self.db[followeeId]["followers"].add(followerId)
        self.db[followerId]["following"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.db and followeeId in self.db:
            if followeeId in self.db[followerId]["following"]:
                self.db[followerId]["following"].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter:
    """
    Revisited on 10/2/2024
    using the heap solution suggested by Neetcode,
    https://neetcode.io/problems/design-twitter-feed
    but a slight difference where the tweets are kept per user in the self.users dict,
    and uses a max heap, with the 
    count of tweets set to negative right before pushing into the max heap.
    Time: O(10LogK * KLogK), where K is the amount of tweets in each following list, and 10 is the amount of tweets that we need
    to retrieve in the newsfeed. 
    The 10LogK is because in the while (maxHeap) loop, we might need to do a heappush, which is LogK,
    up to 10 times. 
    Whereas for KLogK, that is the initial loop where we push the last index of each tweet list from each user onto the maxheap.
    Space: O(N), where N is the total amount of tweets made
    """
    import heapq
    def __init__(self):
        self.users = {}
        self.numTweets = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if (userId not in self.users):
            self.users[userId] = {"tweets": [], "followers": set(), "following": set()}
        self.users[userId]["tweets"].append((self.numTweets, tweetId))
        self.numTweets += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        at the time of the call, create the news feed so it takes into account
        changes to the users followings
        """
        if (userId not in self.users):
            self.users[userId] = {"tweets": [], "followers": set(), "following": set()}
        maxHeap = []
        res = []

        # we include the user themselves into the "following" list
        # since we need to include the users' own tweets in their newsfeed
        self.users[userId]["following"].add(userId)

        # the algorithm involves pushing the last tweet in each individual
        # list of tweets to the max heap, and then popping them out until
        # 10 are reached. However, if 10 tweets are not reached, we then
        # decrement the indices and take the second to last tweet of each
        # list, etc
        for followeeId in self.users[userId]["following"]:
            tweets = self.users[followeeId]["tweets"]
            # if this user has no tweets, continue
            if (len(tweets) == 0):
                continue
            # we start from the back as this will be the most "recent" tweet
            index = len(tweets) - 1
            count, tweetId = tweets[index]
            # we include the count (negative since it's a max heap),
            # the tweetId, followeeId (so we can retrieve the next set of tweets from this user in the 
            # while loop below),
            # as well as the index (decrement by one since, if we need to retrieve the next set),
            # it'll be this index
            heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
        while (maxHeap and len(res) < 10):
            _, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                # retrieve the next most recent tweet from this user
                count, tweetId = self.users[followeeId]["tweets"][index]
                heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.users):
            self.users[followerId] = {"tweets": [], "followers": set(), "following": set()}
        if (followeeId not in self.users):
            self.users[followeeId] = {"tweets": [], "followers": set(), "following": set()}

        """ add the followeeId to the userId's 'following' list"""
        self.users[followerId]["following"].add(followeeId)
        """ vice versa, also add the followerId to the followee's list of followers """
        self.users[followeeId]["followers"].add(followerId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.users):
            self.users[followerId] = {"tweets": [], "followers": set(), "following": set()}
        if (followeeId not in self.users):
            self.users[followeeId] = {"tweets": [], "followers": set(), "following": set()}
        if followerId in self.users[followeeId]["followers"]:
            self.users[followeeId]["followers"].remove(followerId)
        if followeeId in self.users[followerId]["following"]:
            self.users[followerId]["following"].remove(followeeId)

class Twitter:

    def __init__(self):
        """

        """
        self.users = dict()
        self.numTweet = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.users:
            if "tweets" in self.users[userId]:
                self.users[userId]["tweets"].add((tweetId, self.numTweet))
            else:
                self.users[userId]["tweets"] = set()
                self.users[userId]["tweets"].add((tweetId, self.numTweet))
            self.numTweet += 1
        else:
            self.users[userId] = {
                "tweets": set()
            }
            self.users[userId]["tweets"].add((tweetId, self.numTweet))
            self.numTweet += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # generate the news feed on each getNewsFeed call 
        # to take into account new followers/unfollowed and new tweets
        # but this probably isn't very efficient in real life (should pre-generate these)
        
        # get the tweets from the user
        # get the tweets list of each user on the "following" list
        tweetList = []
        if userId in self.users:
            if "tweets" in self.users[userId]:
                tweetList = list(self.users[userId]["tweets"])
            if "following" in self.users[userId]:
                for followedUser in self.users[userId]["following"]:
                    if "tweets" in self.users[followedUser]:
                        tweetList.extend(list(self.users[followedUser]["tweets"]))
            # order them by most recent and get the top 10 (reverse order)
            sortedTweetList = sorted(tweetList, key = lambda twt: twt[1], reverse=True)[:10]
            return [tweet[0] for tweet in sortedTweetList]
        return []

    def follow(self, followerId: int, followeeId: int) -> None:
        # initialize
        if followerId not in self.users:
            self.users[followerId] = {}     
        if followeeId not in self.users:
            self.users[followeeId] = {}
        if "following" not in self.users[followerId]:
            self.users[followerId]["following"] = set()
        if "followers" not in self.users[followeeId]:
              self.users[followeeId]["followers"] = set()
                
      
        # followee Id is being followed by follwower Id
        if followerId not in self.users[followeeId]["followers"]:
            self.users[followeeId]["followers"].add(followerId)
        # follower Id is now following followee id
        if followeeId not in self.users[followerId]["following"]:
            self.users[followerId]["following"].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        # remove the follower from the followers list
        if followeeId in self.users and "followers" in self.users[followeeId] and followerId in self.users[followeeId]["followers"]:
            self.users[followeeId]["followers"].remove(followerId)
        # remove the followee from the following list
        if followerId in self.users and "following" in self.users[followerId] and followeeId in self.users[followerId]["following"]:
            self.users[followerId]["following"].remove(followeeId)
      

            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)