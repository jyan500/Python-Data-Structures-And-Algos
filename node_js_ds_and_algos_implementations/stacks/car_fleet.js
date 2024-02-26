/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
 /*
 some JS differences:
 1) You can store the position and speed as an object, and push to the resulting list
 1) Need to write the sort key manually to sort the list of objects containing position and speed
 */
var carFleet = function(target, position, speed) {
    const sortKey = (a, b) => {
        if (a.position < b.position){
            return 1
        }
        else if (a.position > b.position){
            return -1
        }
        else {
            if (a.speed < b.speed){
                return 1
            }
            else if (a.speed > b.speeD){
                return -1
            }
            else {
                return 0
            }
        }
        return 0
    }
    let sorted = []
    // position and speed arrays have the same length
    for (let i = 0; i < position.length; ++i){
        sorted.push({
            position: position[i],
            speed: speed[i]
        })
    }
    sorted.sort(sortKey)
    let stack = []
    for (let i = 0; i < sorted.length; ++i){
        let timeToReachTarget = (target - sorted[i].position)/sorted[i].speed
        stack.push(timeToReachTarget)
        // if the car in back (stack[-1]) takes less time to reach the target
        // than the car in front (stack[-2]), this will result in a collision,
        // so we pop the top of the stack, and stack[-2] will become the new time,
        // as this is the faster car of the two, and becomes the speed of the fleet.
        if (stack.length >= 2 && stack[stack.length-1] <= stack[stack.length-2]){
            stack.pop()
        }
    }
    return stack.length
};