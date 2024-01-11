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