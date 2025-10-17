from collections import defaultdict
from typing import List


class Twitter:
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


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
