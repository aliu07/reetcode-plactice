import heapq
from collections import defaultdict
from typing import List


class Twitter1:
    """
    Intuition:
        Let us think of the data structures we need to solve this problem. Firstly,
        we need to be able to track tweets chronologically. Therefore, we need a
        monotonically increasing counter/cursor (called time in our soln) to tag each
        tweet. Then, we need a way to store relations between users. We can use dict-
        ionaries for this. Lastly, we need a way to store tweets. We can also use a
        dictionary for this.

        postTweet:
            Update the tweet mappins and increment our time cursor.

        getNewsFeed:
            We get all the tweets of the current user as well as all the tweets of
            each of the user's followees. Then, we sort all these tweets by time in
            reverse order and return the 10 first elements representing the 10 most
            recent tweets.

        follow:
            We can update the mappings accordingly. We don't want to follow ourselves
            since we would pull in duplicate tweets in getNewsFeed when iterating over
            all the followees.

        unfollow:
            We call discard() instead of remove() as discard() does not throw an
            error if the element is not present in the set.


    Runtime:
        postTweet:
            O(1) to update the mapping and increment time.

        getNewsFeed:
            Let n be the number of users and t be the number of tweets.

            It takes O(t) to fetch the user's tweets and to extend it. This is because
            in the worst case, the user follows everyone else and so we need to fetch
            all existing tweets.

            Then, it takes O(t log t) to sort the list.

            Thus, the overall runtime is bounded by O(t log t).

        follow:
            O(1) to update the mapping

        unfollow:
            O(1) to update the mapping.

    Memory:
        Let k be the max number of followees among all users and m be the max number
        of tweets a user has.

        We need O(n * k) memory to store the followMap hashmap.

        We need O(n * m) memory to store the tweetMap hashmap.

        Overall, have a memory complexity of O(n * k + n * m) = O(n * (k + m))
    """

    def __init__(self):
        # keep track of chronological ordering
        self.time = 0
        # userId -> set of people user follows
        self.followMap = defaultdict(set)
        # userId -> [(time, tweetId), ...]
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for f in self.followMap[userId]:
            feed.extend(self.tweetMap[f])

        # sort by reverse chronological order based on time
        feed.sort(key=lambda x: -x[0])
        return [tid for _, tid in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)


class Twitter2:
    """
    Intuition:
        Instead of sorting to get the news feed, we can use a maxHeap to have the most
        recent tweet at the root upon each iteration.

        postTweet:
            Same as Twitter1.

        getNewsFeed:
            We can build our heap using streams of tweets coming from the current user
            AND all of the followees of the current user.

            Each user's most recent tweet will be found at the last index in the list
            stored for that user in the tweetMap hashmap. We build the initial state of
            the max heap by using the most recent tweet of each stream.

            Then, while we have tweets and the feed has not reached capacity, we can
            pop the root and add it to our result. We then take the next element in
            line from that stream.

            For example, if we just popped the most recent tweet from our heap and it
            belongs to user1, we simply push the next most recent tweet in user1's stream
            onto the heap and continue the process.

        follow:
            Same as Twitter1.

        unfollow:
            Same as Twitter1.


    Runtime:
        postTweet:
            Same as Twitter1.

        getNewsFeed:
            Let k be the max number of followees among all users.

            It takes O(1) to follow ourselves.

            It takes O((k + 1) * log (k + 1)) to build the initial max heap. We have
            k + 1 since we include the followees AND the current user.

            We then need up to 10 iterations to collect our feed. Each iteration
            requires at most a pop and a push operation. Pushing/popping takes
            O(log (k + 1)) as outlined previously. Thus, the runtime for this step
            is O(10 * log (k + 1)) ~ O(log (k + 1))

            Thus, the overall runtime is bounded by O((k + 1) * log (k + 1)).

        follow:
            Same as Twitter1.

        unfollow:
            Same as Twitter1.

    Memory:
        Same as Twitter1. O(n * k + n * m) = O(n * (k + m)).
    """

    def __init__(self):
        # keep track of chronological ordering
        self.time = 0
        # userId -> set of people user follows
        self.followMap = defaultdict(set)
        # userId -> [(time, tweetId), ...]
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # add curr user to curr user's followees to include
        # as valid stream of tweets
        self.follow(userId, userId)
        # build maxHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # take last elmt which is most recent
                ix = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][ix]
                heapq.heappush(maxHeap, (-time, tweetId, followeeId, ix - 1))

        while maxHeap and len(res) < 10:
            _, tweetId, followeeId, ix = heapq.heappop(maxHeap)
            res.append(tweetId)

            if ix >= 0:
                time, tweetId = self.tweetMap[followeeId][ix]
                heapq.heappush(maxHeap, (-time, tweetId, followeeId, ix - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
