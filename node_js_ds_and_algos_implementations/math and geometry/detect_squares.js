class CountSquares {
    /* 
    Revisited 9/24/2026
    Key insight:
    Keep a hashmap of all x,y points where the x,y is the key and the frequency is the value

    Given the point in the count() function below, (px, py)
    Check the other points that were added into this.pts (x, y)

    The rule is that given the points x,y and our set point (px, py),
    if abs(px - x) === abs(py, y) exists AND px !== x AND py !== y, this means
    this is a valid diagonal for a square. 

    For example
    (1, 2)     (2, 2) 

    (1, 1)     (2, 1)

    If given px, py as (2,1),
    then we are searching if (1,2 ) exists by checking
    abs(2-1) === abs(1-2) = 1, and px, x and py, y can't be equal to each other (since that
    would mean all the points are stacked on top of each other, which is not a square)

    If that exists, then we can search for the "other diagonal" of the square by simply taking 
    the "reflection" point and searching it in our hashmap, which is
    (x, py) and (px, y), which in this case, is
    (1,1) and (2,2)

    We then multiply the results together which tells us the amount of squares that can be made,
    since we have to take into account that there could be different amounts of each point.
    For example, if (2,2) exists twice,
    we would do count(1,1) * count(2,2) which equals two, which makes sense since you can make
    two squares if you have 2 counts of (2,2)

    */
    constructor() {
        this.pts = []
        this.ptsCount = {}
    }

    /**
     * @param {number[]} point
     * @return {void}
     */
    add(point) {
        let [x,y] = point
        let rep = `${x},${y}`
        this.ptsCount[rep] = (this.ptsCount[rep] || 0) + 1
        this.pts.push(point)
    }

    /**
     * @param {number[]} point
     * @return {number}
     */
    count(point) {
        let [px, py] = point
        let res = 0
        for (let [x,y] of this.pts){
            // ensure we apply logic on valid diagonals only
            if (Math.abs(px-x) !== Math.abs(py-y) || y === py || x === px){
                continue
            }
            let otherDiag1= `${x},${py}`
            let otherDiag2 = `${px},${y}`
            res += (this.ptsCount[otherDiag1] || 0) * (this.ptsCount[otherDiag2] || 0)
        }
        return res
    }
}

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