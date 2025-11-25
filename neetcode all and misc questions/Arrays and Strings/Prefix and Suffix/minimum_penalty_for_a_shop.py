class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        https://neetcode.io/solutions/minimum-penalty-for-a-shop
        iterate through 0 ... n - 1
        calculate the penalty incurred at each index

        This is an O(N^2) operation since in order to calculate the penalty,
        you have to iterate over 0 ... n - 1 in order to know whether
        the value at each index is "Y" or "N"

        how do we address this bottleneck?

        Prefix and Suffix sums:
        If we track two different lists, the prefix of N and the suffix of Y,
        we know exactly how many Y appear after each index i, and how many
        N appear before each index i, so the penalty at any given index i
        is just prefix[i] + suffix[i]

        note that the tricky part is recognizing that our prefix and suffix array
        have to be the len(customers) + 1, since its possible that we evaluate
        the hour at len(customers)+1

        Time: O(N)
        Space: O(N)
        """

        """
        brute force solution
        O(N^2)
        closingTime = 0
        minPenalty = float("inf")
        for i in range(len(customers)+1):
            penalty = 0
            # closing at i hour
            hour = i
            for j in range(len(customers)):
                # once the shop is closed, if customers come, increase the penalty
                if i <= j:
                    if customers[j] == "Y":
                        penalty += 1
                # when the shop is open, but no customers come, increase penalty
                else:
                    if customers[j] == "N":
                        penalty += 1
                    
            if penalty < minPenalty:
                minPenalty = penalty
                closingTime = hour
        return closingTime
        """
        """
        optimized solution using prefix and suffix sums
        """
        prefix = []
        suffix = [0] * (len(customers)+1)

        count = 0
        for c in customers:
            # start out at 0
            prefix.append(count)
            if c == "N":
                count += 1
        # to account for the time when the store closes at the last hour,
        # append the count of N previously
        prefix.append(count)

        # count the suffix of Y        
        for i in range(len(customers)-1,-1,-1):
            if customers[i] == "Y":
                suffix[i] = suffix[i+1] + 1
            else:
                suffix[i] = suffix[i+1]
        print(prefix)
        print(suffix)
        minPenalty = float("inf")
        closingTime = 0
        for i in range(len(customers)+1):
            penalty = suffix[i] + prefix[i]
            if penalty < minPenalty:
                minPenalty = penalty
                closingTime = i
        return closingTime