/*
https://www.youtube.com/watch?v=bahebearrDc
Approach:
1) Use a hashmap to keep track of the frequency of all x, y points, as well as an
array to keep track of all points that we've added so far (since we need to handle duplicates)
2) The trick to detecting a square is figuring out whether the "diagonal" point exists 
given the parameter point (x2, y2). We can do this by iterating through all points we've added so far,
and then doing Math.abs(y2-y1) === Math.abs(x2-x1), which means the distance between y and x is the same.

Then, we just need to check whether the other two points (x2, y1) and (y2, x1) exist, this would form a square
since all four points exist in the map.

3) Because we allow duplicates, we also take into account that we may have duplicates of (x2, y1) and (y2, x1),
so to figure out the total amount of squares we can form, it'd be the frequency of (x2, y1) * frequency of (y2, x1)

Time: O(N)
Space: O(N)
*/
var DetectSquares = function() {
    this.map = {}
    this.points = []
};

/** 
 * @param {number[]} point
 * @return {void}
 */
DetectSquares.prototype.add = function(point) {
    let key = `${point[0]},${point[1]}`
    if (key in this.map){
        ++this.map[key]
    }
    else {
        this.map[key] = 1
    }
    this.points.push(`${point[0]},${point[1]}`)
};

/** 
 * @param {number[]} point
 * @return {number}
 */
DetectSquares.prototype.count = function(point) {
    let res = 0
    for (let p of this.points){
        let k = p.split(",")
        let x1 = parseInt(k[0])
        let y1 = parseInt(k[1])
        let [x2, y2] = point
        if (Math.abs(y2-y1) === Math.abs(x2-x1) && y1 !== y2 && x1 !== x2){
            if (`${x2},${y1}` in this.map && `${x1},${y2}` in this.map){
                res += (this.map[`${x2},${y1}`] * this.map[`${x1},${y2}`]) 
            }
        }
    }
    return res
};

/** 
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */