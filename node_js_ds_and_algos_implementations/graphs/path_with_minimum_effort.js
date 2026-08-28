class Solution {
    /**
     * @param {number[][]} heights
     * @return {number}
     */
    minimumEffortPath(heights) {
        /* 
        Djikstra's Algorithm + Memoization 
        Note that it's max height difference between two consecutive cells,
        so we store the max height difference we found so far as a part of the min heap,
        so that way we're looking for the "min" of those values and popping them out
        */

        let M = heights.length
        let N = heights[0].length
        let minHeap = new MinPriorityQueue(x => x[0])
        minHeap.enqueue([0,0,0])
        // in order to prevent revisiting paths,
        // save the minimum effort that we've found so far,
        // then in different pathways, we compare the minimum effort
        // found between other consecutive cells, and the cell
        // we're trying to visit. If we find another path with smaller effort,
        // re-update
        let memo = Array.from({ length: M }, () => {
            return Array(N).fill(Number.POSITIVE_INFINITY)
        })
        memo[0][0] = 0
        const directions = [[0,1], [0,-1], [1,0], [-1,0]]

        const inBounds = (i,j) => {
            return 0 <= i && i < M && 0 <= j && j < N
        }

        while (!minHeap.isEmpty()){
            const [diff, i, j] = minHeap.dequeue()
            if (i === M - 1 && j === N - 1){
                return diff
            }
            // if we already found an optimal path, we don't need to re-explore
            if (memo[i][j] < diff){
                continue
            }
            for (let [x,y] of directions){
                const newX = x + i
                const newY = y + j
                if (inBounds(newX,newY)){
                    const newDiff = Math.max(diff, Math.abs(heights[i][j] - heights[newX][newY]))

                    // if we've calculated a max absolute difference
                    // that's less than the current, update it 
                    if (newDiff < memo[newX][newY]){
                        memo[newX][newY] = newDiff
                        minHeap.enqueue([newDiff, newX, newY])
                    }
                }
            }
        }

        // in the case there's only one column + row element and we can't explore
        // just return 0
        return 0
    }
