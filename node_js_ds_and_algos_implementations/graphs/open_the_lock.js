class Solution {
    /**
     * @param {string[]} deadends
     * @param {string} target
     * @return {number}
     */
    openLock(deadends, target) {
        /* 
        Thought process:
        Left and right sequential doesn't work:
        For example, if we took a left to right sequential approach,
        if we had target 4444, with the following deadends
        ["4443","4445","4434","4454","4344","4544","3444","5444"]
        the two actual blockers are 4443 and 4445, because we can get 4440 since
        it's not in the deadends (i.e increasing 0 -> 4 for each digit along the way with no problems)

        However, say if 4440 was in the deadends, then its not possible
        to do the left to right sequential, we'd have to do 
        3440, increase one side first, then increase 3 to 4.

        It seems at any given iteration, we can increase or decrease any one of the 4 slots
        like so, and then check if that current combination is in the deadends or not.

        Backtracking approach:
        I realized midway through writing it that there's not really a solid
        stopping point, since the elements loop around, you don't know whether
        to stop at a certain point, or continue 
        
        Shortest path with BFS approach:
        This is the right approach, since you're looking for the shortest distance,
        and each particular "turn" represents an edge within a graph, you don't need an adjacency list,
        and can calculate the neighbors on the fly.
        By default, the moment you reach the target, you would've found the shortest distance
        when using BFS

        O(E+V), but actually simplifies down to O(N), because the amount of edges are bounded by 10^4, where there are 10 different combinations (0 to 9),
        and 4 different positions
        */

        let q = []
        deadends = new Set([...deadends])
        let visited = new Set()
        q.push({
            cur: [0,0,0,0],
            turns: 0
        })
        while (q.length){
            const {cur, turns} = q.shift()
            // once you reach a dead end, you won't be able to continue further
            // down this path
            let str = cur.join("")
            if (deadends.has(str)){
                continue
            }
            if (str === target){
                return turns
            }
            // calculate all neighbors i.e 0001, 0010, 0100, 1000, 9000, 0900, etc
            for (let i = 0; i < cur.length; ++i){
                let increment = cur[i] + 1 <= 9 ? cur[i] + 1 : 0
                let decrement = cur[i] - 1 >= 0 ? cur[i] - 1 : 9
                // splice without modifying the original
                let incremented = cur.toSpliced(i, 1, increment)
                let decremented = cur.toSpliced(i, 1, decrement)
                if (!visited.has(incremented.join(""))){
                    visited.add(incremented.join(""))
                    q.push({cur: incremented, turns: turns + 1})
                }
                if (!visited.has(decremented.join(""))){
                    visited.add(decremented.join(""))
                    q.push({cur: decremented, turns: turns + 1})
                }
            }
        }
        return -1
    }
}
