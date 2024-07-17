/**
 * @param {number} rowIndex
 * @return {number[]}
 */
/*
Approach:
The pattern starts from i = 2, given the previous row,
for each index k between the first and last index of the current row, 
    current[k] = previous[k-1] + previous[k]

    1   i = 0
   1  1 i = 1
        i = 2
    
    prev starts at [1, 1]

for i = 2 ... rowIndex
1) at a given level, we can set our current level i to have the same number of 1's plus an additional one
    so for i = 2, we need 3 1's in the current level

    i.e cur = [1, 1, 1]
2) for k = 1 ... k <= i - 1, this means everything but the first and last index of the current level
    cur[k] = prev[k-1] + prev[k]
    
    in this case, k = 1, so prev[0] + prev[1] = 2
    cur = [1, 2, 1]
3) then, set the previous to be the current

    prev = [1, 2, 1]

Once i reaches rowIndex, we return prev

returns [1, 2, 1]

Time:
O(N)

Space:
O(N)

*/
var getRow = function(rowIndex) {
    if (rowIndex === 0){
        return [1]
    }
    else if (rowIndex === 1){
        return [1, 1]
    }
    let prev = [1, 1]
    for (let i = 2; i <= rowIndex; ++i){
        let cur = []
        let numCols = i + 1
        for (let j = 0; j < numCols; ++j){
            cur.push(1)
        }
        for (let k = 1; k <= i-1; ++k){
            cur[k] = prev[k-1] + prev[k]
        }
        prev = [...cur]
    }
    return prev
};