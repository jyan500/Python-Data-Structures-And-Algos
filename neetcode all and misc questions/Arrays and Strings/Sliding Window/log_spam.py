"""
(Not a leetcode question but was asked this during an interview.)
Given a list of JSON objects containing a user ID and timestamp in milliseconds, N representing the limit on the 
amount of requests, and K representing a time range in milliseconds, 
return all user IDs that have made >= N requests within a span of K milliseconds,
these user IDs would be flagged as "spam".
Assume the data is sorted by timestamp ascending.
 
Input:
[
	{"userId": 1, "timestamp": 1},
	{"userId": 1, "timestamp": 2},
	{"userId": 1, "timestamp": 3},
	{"userId": 2, "timestamp": 4},
	{"userId": 1, "timestamp": 590},
	{"userId": 1, "timestamp": 600},
	{"userId": 4, "timestamp": 700},
	{"userId": 1, "timestamp": 998},
	{"userId": 4, "timestamp": 2001},
	{"userId": 4, "timestamp": 2002},
	{"userId": 1, "timestamp": 2003},
	{"userId": 2, "timestamp": 2004},
	{"userId": 3, "timestamp": 2205},
	{"userId": 4, "timestamp": 2305},
	{"userId": 4, "timestamp": 2799},
	{"userId": 4, "timestamp": 2800},
]
 
N = 5
K = 1000
 
Output:
[1, 4]
 
Explanation:
userId 1 makes 5 requests between 1 and 1001 milliseconds, meaning this user has made >= 
5 requests in this time range.
userId 4 makes 5 requests between 2001 and 3001 milliseconds, meaning this user has made >= 5 requests
in this time range.
 
Input:
[
	{"userId": 1, "timestamp": 1},
    {"userId": 2, "timestamp": 1},
    {"userId": 3, "timestamp": 1},
	{"userId": 1, "timestamp": 2},
	{"userId": 1, "timestamp": 3},
	{"userId": 2, "timestamp": 4},
	{"userId": 1, "timestamp": 1590},
	{"userId": 1, "timestamp": 1600},
	{"userId": 4, "timestamp": 1700},
	{"userId": 1, "timestamp": 1998},
	{"userId": 4, "timestamp": 5001},
	{"userId": 4, "timestamp": 5002},
	{"userId": 1, "timestamp": 5003},
	{"userId": 2, "timestamp": 5004},
	{"userId": 3, "timestamp": 5205},
	{"userId": 4, "timestamp": 5305},
	{"userId": 4, "timestamp": 5799},
	{"userId": 4, "timestamp": 5800},
]
N = 5
K = 1000
 
Output:
[4]
 
Explanation:
userId 4 makes 5 requests between 5001 and 6001 milliseconds, meaning this user has made >= 5 requests
in this time range.
"""

"""
Approach:
sliding window strategy using two pointers, left and right. Where the left represents the beginning of
our current window, and r represents our current timestamp

the one trick with this problem is that if we reach a time that is outside of our current window,
we have to use a while loop to "catch" the left pointer up until the left most timestamp + span >= current timestamp,
to ensure that our current timestamp is within the given time span window.

At each iteration of the inner while loop, we also decrement the count of the user id of the entry represented by the left most pointer

Time: O(N) (although ONLogN for sorting if the input is not pre-sorted)
Space: O(N)

"""

def detectSpam(logs: [dict], limit: int, milliseconds: int):
    from collections import defaultdict
    # if amount of logs < limit, there aren't enough
    # requests to be considered spam, so return empty array
    if (len(logs) < limit):
        return []
    logs.sort(key=lambda x: x["timestamp"])
    res = set()
    l = 0
    counter = defaultdict(int)
    # initialize count for the first log entry
    counter[logs[l]["userId"]] += 1
    for r in range(1, len(logs)):
        userId = logs[r]["userId"]
        timestamp = logs[r]["timestamp"]
        # if the current timestamp is not in our time window
        # update the window by incrementing the left pointer
        # until our current time is within the window
        while timestamp > logs[l]["timestamp"] + milliseconds:
            # remove the entry at the left most pointer
            counter[logs[l]["userId"]] -= 1
            l += 1
        # add user id to the hashmap and keep track of count
        counter[userId] += 1
        # if the amount in this window exceeds the limit,
        # add to result
        if counter[userId] >= limit:
            res.add(userId)

    return list(res)

print(detectSpam(
	[
		{"userId": 1, "timestamp": 1},
        {"userId": 2, "timestamp": 1},
        {"userId": 3, "timestamp": 1},
		{"userId": 1, "timestamp": 2},
		{"userId": 1, "timestamp": 3},
		{"userId": 2, "timestamp": 4},
		{"userId": 1, "timestamp": 1590},
		{"userId": 1, "timestamp": 1600},
		{"userId": 4, "timestamp": 1700},
		{"userId": 1, "timestamp": 1998},
		{"userId": 4, "timestamp": 5001},
		{"userId": 4, "timestamp": 5002},
		{"userId": 1, "timestamp": 5003},
		{"userId": 2, "timestamp": 5004},
		{"userId": 3, "timestamp": 5205},
		{"userId": 4, "timestamp": 5305},
		{"userId": 4, "timestamp": 5799},
		{"userId": 4, "timestamp": 5800},
	], 5, 1000
))

# expected answer is [4]
print(detectSpam(
[
    {"userId": 1, "timestamp": 1},
    {"userId": 1, "timestamp": 2},
    {"userId": 1, "timestamp": 3},
    {"userId": 2, "timestamp": 4},
    {"userId": 1, "timestamp": 590},
    {"userId": 1, "timestamp": 600},
    {"userId": 4, "timestamp": 700},
    {"userId": 1, "timestamp": 998},
    {"userId": 4, "timestamp": 2001},
    {"userId": 4, "timestamp": 2002},
    {"userId": 1, "timestamp": 2003},
    {"userId": 2, "timestamp": 2004},
    {"userId": 3, "timestamp": 2205},
    {"userId": 4, "timestamp": 2305},
    {"userId": 4, "timestamp": 2799},
    {"userId": 4, "timestamp": 2800},
], 5, 1000))

# expected answer is [1,4]




