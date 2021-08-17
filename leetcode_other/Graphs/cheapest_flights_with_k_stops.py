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
        
