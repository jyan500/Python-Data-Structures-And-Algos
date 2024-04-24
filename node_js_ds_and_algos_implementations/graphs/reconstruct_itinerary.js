/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    /*
    Neetcode 
    DFS (This solution makes the most sense but TLE's on Leetcode)
    The most optimized version uses Eulerian Paths Algorithm:
    https://cp-algorithms.com/graph/euler_path.html
 
    Time Complexity:
    (O(V+E)^d), we're running DFS, but we also need to backtrack potentially, meaning
    we may need to revisit the same edge multiple times. This could take d amount of times, depending on the amount of destinations for the given source
    Space Complexity:
    O(E), size of the call stack based on the amount of edges
    
    1) Sort the list of tickets by their destinations in ascending alphabetical order to meet the lexical order requirement
    2) build adjacency list based on tickets,
    where the key is the "from" and the value is an array
    of destinations (i.e "to's")
    tickets = [[from, to], [from, to], ...]
    adjacency = {from: [to, to, ...], from: [to, to, ...]}
    3) Apply DFS starting from "JFK" as stated in the requirements
    4) Within DFS:
        make a copy of the value (based on adjacency[key])
        loop through all destinations from adjacency[key] from our "from" source that is passed into DFS
            when visiting a destination, to note that we've visited it, we'll make a copy
            of the adjacency list value, and do list.pop() based on the destination's index.
            Also add the destination in the results list
            run DFS(), if it returns true, we can also return true out of this loop once
            we've found an answer. Note that we're mutating the value of adjacency list directly.
            
            if DFS() does not return true, we need to continue searching the other values in the loop. In that case, put the destination back into the adjacency list, and remove it from the results list
    */
    let adjacency = {}
    let sortKey = function(tickets1, tickets2){
        let dest1 = tickets1[1]
        let dest2 = tickets2[1]
        if (dest1 < dest2){
            return -1
        }
        else if (dest1 > dest2){
            return 1
        }
        else {
            return 0
        }
    }
    tickets.sort(sortKey)
    for (let [from, to] of tickets){
        if (!(from in adjacency)){
            adjacency[from] = []
        }
        adjacency[from].push(to)
    }
    let res = ["JFK"]
    var dfs = function(src){
        // if we've visited all edges, return true (+1 since res always has JFK as the start)
        if (res.length === tickets.length + 1){
            return true
        }
        // if this source does not have any destinations, return false
        if (!(src in adjacency)){
            return false
        }
        let temp = [...adjacency[src]]
        // note because we're changing adjacency list, we need to make the copy temp here
        for (let i = 0; i < temp.length; ++i){
            // remove this particular destination within the destination list
            // based on the index
            let dest = temp[i]
            adjacency[src].splice(i, 1)
            res.push(dest)
            // if we've visited every destination, return true to break out
            // of the loop
            if (dfs(dest)){
                return true
            }
            adjacency[src].splice(i, 0, dest)
            res.pop()
        }
        return false
    }
    dfs("JFK")
    return res
};