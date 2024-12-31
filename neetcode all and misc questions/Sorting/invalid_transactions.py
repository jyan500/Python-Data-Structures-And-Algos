class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        Approach:
        https://leetcode.com/problems/invalid-transactions/
        Time: O(N^2 * NLogN * K), where K is the amount of keys in nameMap
        Space: O(N)
        1) parse list of transactions by splitting by "comma"
        2) keep two hash maps, one then maps each transaction based on the name
        and another that maps the original string transaction to its index
        3) Keep a set of the indices of each invalid transaction
        4) Loop through the first hashmap, parsing through the transactions by name.
            Sort each transaction list by the start
            Do a nested for loop to check whether the time difference between 
            each transaction is <= 60 and if they're in different cities,
            if so add both indices to the set.
        5) Map each indices stored in the set back to the original string transaction. We do this
        to avoid duplicates, as well as avoiding situations where two strings have the same value,
        but are on different indices.

        """
        from collections import defaultdict
        nameMap = defaultdict(list)
        transactionIndices = defaultdict(str)
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            nameMap[name].append([i, name, int(time), int(amount), city])
            transactionIndices[i] = transactions[i]
        invalidTransactions = set()
        for key in nameMap:
            nameMap[key].sort(key=lambda x: (x[1], x[2]))
            transactionList = nameMap[key]
            for l in range(len(transactionList)):
                if transactionList[l][3] > 1000:
                    index,name, time, amount, city = transactionList[l]
                    invalidTransactions.add(index)
                for r in range(l+1, len(transactionList)):
                    index, name, time, amount, city = transactionList[r]
                    prevIndex, prevName, prevTime, prevAmount, prevCity = transactionList[l]
                    if (time - prevTime <= 60 and prevCity != city):
                        invalidTransactions.add(index)
                        invalidTransactions.add(prevIndex)
        invalidTransactions = [transactionIndices[index] for index in invalidTransactions]
        return invalidTransactions

        