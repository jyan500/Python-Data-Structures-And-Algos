/*
Approach:
Keep a DB that contains userIds as keys, and values as {feed: MaxPriorityQueue, followers: set(), following: set()}

We initialize a class wide timestamp variable to use as priority in the priority queue feed

create post
    push the post onto the tweets array
    
    Time complexity:
    O(1)
    
get news feed
    retrieve the posts made by the user and followee's
    enqueue onto the feed 
    O(NLogN), where N is the amount of posts in the feed

follow
    add the follower to the followee's follower list
    add the followee to the follower's following list
    O(1)
    

unfollow
    remove the follower from the followee's follower list
    remove the followee from the follower's following list
    O(1)


*/
var Twitter = function() {
    this.db = {}
    this.timestamp = 1
};

/** 
 * @param {number} userId 
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function(userId, tweetId) {
    if (!(userId in this.db)){
        this.db[userId] = {"tweets": [], "followers": new Set(), "following": new Set()}
    } 
    this.db[userId].tweets.push({timestamp: this.timestamp, tweetId: tweetId, userId: userId})
    this.timestamp++
};

/** 
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function(userId) {
    // generate the news feeds on request based on the users' own posts and the 
    // followee's posts
    let res = []
    if (userId in this.db){
        let feed = new MaxPriorityQueue({priority: (p) => p.timestamp})
        let tweets = [...this.db[userId].tweets]
        for (let followeeId of this.db[userId].following){
            tweets = [...tweets, ...this.db[followeeId].tweets]
        }
        for (let tweet of tweets){
            feed.enqueue(tweet)
        }
        return feed.toArray().slice(0, 10).map((t) => t.element.tweetId)
    }
    return res
};

/** 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function(followerId, followeeId) {
    if (!(followerId in this.db)){
        this.db[followerId] = {"tweets": [], "followers": new Set(), "following": new Set()}
    }
    if (!(followeeId in this.db)){
        this.db[followeeId] = {"tweets": [], "feed": new MaxPriorityQueue({priority: (p) => p.timestamp}), "followers": new Set(), "following": new Set()}
    }
    this.db[followerId].following.add(followeeId)
    this.db[followeeId].followers.add(followerId)
    
};

/** 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function(followerId, followeeId) {
    // delete the followerId from the following list for the follower, and delete the follower id from the followers list of the followee
    this.db[followerId].following.delete(followeeId)
    this.db[followeeId].followers.delete(followerId)
};

/** 
 * Your Twitter object will be instantiated and called as such:
 * var obj = new Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */