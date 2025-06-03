class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        https://leetcode.com/problems/friends-of-appropriate-ages/editorial/
        nested loop comparison?

        20 -> 30 is valid? No, because 30 > 20
        20 -> 100 is valid? No, because 100 > 20
        ...

        30 -> 20 is valid? , 20 <= (0.5 * 30) + 7, 20 <= 15+7, 20 <= 22 is false, No
        30 -> 100 is valid? No, because 100 > 30
        ...
        100 -> 30, is valid? No, because 30 <= (0.5*100)+7 is false

        110 -> 110 is valid though because 100 <= (0.5*110) + 7 is true
        120 -> 110 is valid for the same reason, and 120 -> 100

        Optimizations?
        it seems the youngest person in the list cannot send a friend request to anyone else,
        so we can just start from index 1.

        can we check the inverted relationship (both x -> y and y -> x) at the same time to reduce
        repeated work? we could store the pair of indices in the hashmap

        20 -> 30, 30 -> 20
        20 -> 100, 100 -> 20
        20 -> 110, 110 -> 20
        20 -> 120, 120 -> 20

        30 -> 20, we could reference in the hashmap to see that we've already calculated this
        30 -> 100, 100 -> 30
        30 -> 110 ....

        the problem with this approach is that there could be many pairs which is more memory.

        The last optimization (from the editorial) is realizing that instead of looking at pairs 
        of indices, we can look at age groups, and compare the age groups instead. 

        So in a hashmap, say if we have [16, 16, 16, 30, 30, 30, 30]. It makes more sense to group the ages
        together by their count, i.e the (16, 3) and (30, 4) together, and then we can evaluate
        whether friend requests can be sent between these two ages. If so, we just have to multiply
        the count of age1 by the count of age2 to represent the total amount of friend requests that can be sent
        between these two age groups

        Also, we can take into account that the max age is 120 based on the problem statement,
        so after we do an initial pass to get the age groups, we do a nested loop, 0 ... 120,
        0 ... 120, and perform the operation above, comparing the age groups that are in the hashmap
        together.

        Time: O(N), because technically the nested loop comparison is constant (120 * 120), so the only O(N) work is creating the hashmap
        Space: O(120), there can only be at max 120 keys in the hashmap since the age only goes up to 120

        """
        from collections import Counter
        def canSend(age1, age2):
            condition1 = age2 <= ((0.5 * age1) + 7)
            condition2 = age2 > age1
            condition3 = age2 > 100 and age1 < 100
            # if none of these conditions are true, a friend request can be sent
            # normally, if any of condition1 or condition2 or condition3 are true, a request cannot be sent
            return not (condition1 or condition2 or condition3)
            
        # memory limit exceeded
        # calculated = set()
        # res = 0
        # for i in range(len(ages)):
        #     for j in range(len(ages)):
        #         if i != j:
        #             if (i, j) not in calculated and canSend(ages[i], ages[j]):
        #                 res += 1
        #                 calculated.add((i, j))
        #             elif (j, i) not in calculated and canSend(ages[j], ages[i]):
        #                 res += 1
        #                 calculated.add((j, i))
        # return res
        # map the ages to their count
        ageGroups = Counter(ages)
        res = 0
        for i in range(0, 121):
            for j in range(0, 121):
                if i in ageGroups and j in ageGroups and canSend(i, j):
                    if i != j:
                        res += (ageGroups[i] * ageGroups[j])
                    # if the ages are the same, there's an edge case here where you need to subtract
                    # one from the total count of the age groups, since you can't send a friend request to yourself
                    else:
                        res += ((ageGroups[i]-1) * ageGroups[j])

        return res     
        

        

        
