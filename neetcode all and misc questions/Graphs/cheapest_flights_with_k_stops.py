'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

An additional test case which involves a cycle:
5
[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
0
4
1

adjacency list = {0: [3], 1: [2,3], 2: [0, 4], 3: [1,4], 4: [0,2]}
src = 0
dest = 4
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Bellman Ford's Algorithm
        https://www.youtube.com/watch?v=5eIK3zUdYmE
        O(E*K), k is the max amount of stops
        Concept:
        We continually iterate through all flights, the amount of times we iterate is based on k+1 (due to the way the problem is defined,
        traveling across two edges is considered "one" stop)
        and keep track of a prices array to check the smallest price needed to travel from one stop to another
        
        Example:
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        
        initial setup:
        prices = [float('inf'), float('inf'), float('inf')]
        prices[src] = 0
        
        prices = [0, float('inf'), float('inf')]
        
        looping k + 1 times... (2)
        
        outer loop 1st iteration
        i = 0
        tmp = [0, float('inf'), float('inf')]
        
        inner loop 1st iteration 
        [0, 1, 100]
        from = 0, to = 1, price = 100
        prices[from] + price = 0 + 100 = 100
        is 100 < tmp[to] (100 < float('inf')), true
        update tmp[1] = 100
        
        tmp = [0,100,float('inf')]
        
        inner loop 2nd iteration
        [1, 2, 100]
        from = 1, to = 2, price = 100
        prices[from] == float('inf'), continue
        
        inner loop 3rd iteration
        [0, 2, 500]
        from = 0, to = 2, price = 500
        prices[from] + price < tmp[to], 0 + 500 < float('inf'), true
        tmp[to] = prices[from_] + price, tmp[2] = 500
        tmp = [0, 100, 500]
        
        back to outer loop...
        set prices = tmp, prices = [0, 100, 500]
        
        outer loop 2nd iteration
        i = 1
        tmp = [0, 100, 500]
        
        inner loop 1st iteration
        [0, 1, 100]
        from = 0, to = 1, price = 100
        prices[from] + price < tmp[to], 0 + 100 < 100, false, 
        so no need to set tmp
        
        inner loop 2nd iteration
        [1, 2, 100]
        from = 1, to = 2, price = 100
        prices[from] + price < tmp[to], prices[1] + price < tmp[2],
        100 + 100 < 500, true,
        set tmp[2] = 200
        tmp = [0, 100, 200]
        
        inner loop 3rd iteration
        [0, 2, 500]
        from = 0, to = 2, price = 500
        prices[0] + 500 < tmp[2], 0 + 500 < 200, false
        
        inner loop ends
        prices = tmp
        prices = [0, 100, 200]
        
        outer loop also ends
        
        returns prices[dst], prices[2] = 200
        final answer = 200
        """
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            tmp = prices.copy()
            for from_, to, price in flights:
                if prices[from_] == float("inf"):
                    continue
                if prices[from_] + price < tmp[to]:
                    tmp[to] = prices[from_] + price
            prices = tmp
        return -1 if prices[dst] == float("inf") else prices[dst]
        


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Directed graph
        1) build adjacency list
        2) BFS, use queue
        keep track of the number of stops taken within the queue itself in a tuple
        
        Technically this should work but it TLEs in Leetcode
        """
#         from collections import deque
#         adjacencyList = dict()
#         for i in range(n):
#             adjacencyList[i] = []
#         for i in range(len(flights)):
#             fromSrc, toDst, price = flights[i]
#             adjacencyList[fromSrc].append((toDst, price))
        
#         q = deque()
#         minPrice = float("inf")
#         # append all the initial edges starting from src
#         for i in range(len(adjacencyList[src])):
#             to, price = adjacencyList[src][i]
#             # add the 0 to represent the stops taken
#             q.append((to, price, 0))
#         while (q):
#             to, price, numStops = q.popleft()
#             if to == dst and numStops <= k:
#                 minPrice = min(minPrice, price)
#             else:
#                 for neighbor in adjacencyList[to]:
#                     neighborTo, neighborPrice = neighbor
#                     if price + neighborPrice < minPrice:
#                         q.append((neighborTo, price + neighborPrice, numStops + 1))


#         return minPrice if minPrice != float("inf") else -1

        """
        Bellman Ford Solution
        https://www.youtube.com/watch?v=5eIK3zUdYmE&ab_channel=NeetCode
        Time Complexity: 
        O(E * K)
        Space:
        O(E)

        Example:

        [[0, 1, 100], [0, 2, 500], [1, 2, 100]]

               0

            /    \
           1  --  2 

        src = 0 
        dst = 2
        k = 1
        
        1st iteration of "for i in range(k+1)..."
        ---------------------------------------
        prices = [0, inf, inf]
        tmpPrices = [0, inf, inf]
    
        for s, d, p in flights ...
        1st iteration
        s = 0, d = 1, p = 100

        prices[0] + 0 < tmpPrices[0], true

        tmpPrices = [0, inf, inf]

        2nd iteration
        s = 0 d = 2 p = 500

        prices[0] == inf, continue ...

        tmpPrices = [0, inf, 500]

        3rd iteration
        s = 1 d = 2 p = 100

        prices[1] == inf, continue ...

        tmpPrices = [0, 100, 500]

        prices = tmpPrices

        2nd iteration of "for i in range(k+1)"
        ---------------------------------------

        prices = [0, 100, 500]
        tmpPrices = [0, 100, 500]

        for s, d, p in flights...
        1st iteration 
        s = 0 d = 1 p = 100 

        no need to update here, it remains 0 

        2nd iteration
        s = 0 d = 2 p = 500
        
        no need to update here, it remains 0 

        3rd iteration
        s = 1 d = 2 p = 100

        Important!
        prices[1] = 100
        prices[1] + p < tmpPrices[2], true!

        100 + 100 < 500

        tmpPrices[2] = 200

        prices = tmpPrices

        Final result:

        prices[2] = 200
        """
    
        prices = [float("inf")] * n
        prices[src] = 0
        
        # it's k + 1 because 0 "stops" involves at least two nodes
        # 1 "stop" involving at least 3 nodes, etc
        for i in range(k+1):
            # you need the tmpPrices to act as a "buffer" until we finish our loop below so we don't 
            # update prices while we loop through at the same time and get a potentially incorrect answer
            # we only prices after we're done with the below loop
            tmpPrices = prices.copy()
            for s, d, p in flights:
                # if we cannot reach this node in the graph, ignore
                if prices[s] == float("inf"):
                    continue
                # if we can reach node destination (d) in a smaller price, update it
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
            
        

'''
Time complexity: O(V^K), where V is the number of vertices
https://stackoverflow.com/questions/53127792/time-complexity-cheapst-flights-within-k-stops
the algorithm might return to cities that its already visited, up to k times

Space complexity: O(V), since we may need to hold all vertices in the queue
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## create an adjacency list of our edges, storing a tuple where tup[0] is the edge and tup[1] is the price to travel
        ## along that edge
        '''
        {0:[(1, 100, 0),(2, 500, 0)], 1: [(2, 100, 0)], 2:[]}
        
        '''
        adjacency_list = dict()
        ## initialize the keys for the amount of cities
        for i in range(n):
            adjacency_list[i] = []
            
        for i in range(len(flights)):
            city, dest, price = flights[i]
            if (city in adjacency_list):
                adjacency_list[city].append((dest, price))
        memo = dict()
        ans = self.dfs(adjacency_list, src, dst, k, -1, memo)
        if (ans == float('inf')):
            return -1
        else:
            return ans
        
    
    def dfs(self, adjacency_list: dict, src: int, dst: int, k: int, num_stops: int, memo: dict)->int:
        
        if ((src,num_stops) in memo):
            return memo[(src, num_stops)]
        if (src == dst):
            # print('arrived destination')
            # print('num stops: ', num_stops)
            if (num_stops <= k):
                # print('num stops was less than k')
                return 0       
            else:
                return float('inf')
        ## if we've used up all the number of stops available, then there's no solution, just return infinity
        if (num_stops > k):
            return float('inf')
        cost = float('inf')
        for i in range(len(adjacency_list[src])):
            city, travel_price = adjacency_list[src][i]
            # print('next city: ', city)
            # print('travel price: ', travel_price)
            cost = min(cost, travel_price + self.dfs(adjacency_list, city, dst, k, num_stops + 1, memo))
        memo[(src, num_stops)]=cost
        return cost

    def bfs(self, adjacency_list, src, dst, k, num_stops):
    	queue = deque()
        ## append the initial travel options
        for i in range(len(adjacency_list[src])):
            queue.append(adjacency_list[src][i])
        smallest_price = float('inf')
        while (queue):
            edge, price, num_stops = queue.popleft()
            ## if we've reached our destination, and the number of stops that we've taken to reach
            ## this node is less than k
            ## check the smallest price
            if (edge == dst):
                if (num_stops <= k):
                    smallest_price = min(smallest_price, price)
                else:
                    continue
            else:
                ## append the edges that can be traveled to the queue
                ## but also add the current price of the route we're traveling to the edge's price
                ## and increase the number of stops by 1
                for j in range(len(adjacency_list[edge])):
                	if (price2 + price < smallest_price):
	                    edge2, price2, num_stops = adjacency_list[edge][j]
	                    queue.append((edge2, price2 + price, num_stops + 1))
                    
        if (smallest_price == float('inf')):
            return -1
        else:
            return smallest_price
        
