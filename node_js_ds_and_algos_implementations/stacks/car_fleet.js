class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        /*
        Revisited 3/30/2026
        this is similar to an intervals problem
        sort the cars by their position

        then compare current and previous cars based on the time taken
        to reach the target

        if previous takes less time than the current
            that means they will form a fleet
            so combine the two cars and set the speed
            to the slower speed 
        
        target position = cur position + (time * cur speed)
        solve for time
        time = (target position - cur position)/speed

        */
        // sort in reverse order where highest position is first
        let cars = position.map((pos, index) => {
            return [
                pos,
                speed[index]
            ]
        }).sort((a,b) => {
            if (a[0] < b[0]){
                return 1     
            } 
            else if (a[0] > b[0]){
                return -1
            }
            return 0
        })
        let stack = [cars[0]]
        for (let i = 1; i < cars.length; ++i){
            let [prevPos, prevSpeed] = stack[stack.length-1]
            let [curPos, curSpeed] = cars[i]
            let prevTime = (target - prevPos)/prevSpeed
            let curTime = (target - curPos)/curSpeed
            // if it takes less time, it will become a fleet with the car in front of it
            if (curTime <= prevTime){
                // merge
                stack[stack.length-1] = [prevPos, prevSpeed]
            }
            else {
                stack.push(cars[i])
            }
        }
        return stack.length
    }
}

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
};/2026