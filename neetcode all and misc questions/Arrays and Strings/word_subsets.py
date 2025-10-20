class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        brute force
        pseudo code:
        create a hashmap of each word in words 1
        create a hashmap of each word in words2
        for each hashmap in words 1,
            for each hashmap in words 2
                check if key exists in words1 map, if so check if the value of that key in words1 map < words2 map,
                if so, this means it cannot be a valid answer, so break
        return result
        """
        # from collections import Counter
        # words1Maps = [Counter(word) for word in words1]
        # words2Maps = [Counter(word) for word in words2]
        # res = []
        # for i in range(len(words1)):
        #     wordMap = words1Maps[i]
        #     flag = True
        #     for word2Map in words2Maps:
        #         for key in word2Map:
        #             if key not in wordMap or (key in wordMap and wordMap[key] < word2Map[key]):
        #                 flag = False
        #                 break
        #     if flag:
        #         res.append(words1[i])
        # return res

        """
        https://neetcode.io/solutions/word-subsets

        Optimized:
        The trick to this problem is realizing that the bottleneck is that we're creating multiple hashmaps
        for all the words in words2, and then for each word in word 1, we're having to compare each of the
        hashmaps in words2 with words1.

        One idea is to try and merge the hashmaps on words2 together
        You can see on a test case like this:
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["lo", "eo"]

        if we were to treat "lo" and "eo" as one word, you would get "l": 1, "o": 2, "e": 2, 
        you can see that this isn't correct though, as we should be including "leetcode" as an 
        answer here, even though it only has one "o" (but the merged hashmap designates two "o"s)

        The key is realizing we need the MAX of how many times that character can show up, so in this example
        with "lo" and "eo", "o" shows up at most once within each of these words, so the merged hashmap
        should designate "o": 1 instead of "o": 2, which is correct.

        Another example is 
        words1 = ["acaac","cbcbc","aacbb","caacc","bcbbb"]
        words2 = ["c","cc","b"]

        here, if we were to merge the hashmaps together on words2, we would mark
        "c" as appearing at most twice.

        So we can update the solution by creating the hashmaps for words2, and then merging them
        together by getting the max of how many times a given character appears

        Then perform the same idea as the brute force where you check if the occurrences of each character in
        the merged hashmap >= the amount of times the same character appears in the hashmap for each word in words1

        Time Complexity: O(N*L1 + M*L2), where N is the length of words 1, and L1 is the average length of the individual words in words1,
        and M is the length of words 2, and L2 is the average length of the individual words in words2

        Simplifying its about O(N+M), even though we have a nested loop in the code that compares every key of the merged hashmap
        to words1 map, this nested loop actually does O(26) work because of the problem constraint (which mentions its only lower case letters)
        So essentially its doing O(N * 26) for the nested loop

        """
        from collections import defaultdict
        words1Maps = [Counter(word) for word in words1]
        words2Maps = [Counter(word) for word in words2]
        mergedHashmap = defaultdict(int)
        for hashMap in words2Maps:
            for key in hashMap:
                mergedHashmap[key] = max(mergedHashmap[key], hashMap[key])
        res = []
        for i in range(len(words1)):
            wordMap = words1Maps[i]
            flag = True
            for key in mergedHashmap:
                if key not in wordMap or (key in wordMap and wordMap[key] < mergedHashmap[key]):
                    flag = False
                    break
            if flag:
                res.append(words1[i])
        return res