class Solution {
    /**
     * @param {number[]} asteroids
     * @return {number[]}
     */
    asteroidCollision(asteroids) {
        if (!asteroids.length){
            return []
        }
        let stack = [asteroids[0]]
        for (let i = 1; i < asteroids.length; ++i){
            // if top asteroid is right and current is going left
            let exploded = false
            while (stack.length && (stack[stack.length-1] > 0 && asteroids[i] < 0)){
                const diff = asteroids[i] + stack[stack.length-1]
                // if both asteroids collide together, pop out and don't add asteroids[i]
                if (diff === 0){
                    exploded = true
                    stack.pop()
                    break
                }
                // this means the right asteroid is overtaking the left, so we pop
                // and continue checking in the while loop to see if it will continue to overtake
                // the top of the stack
                else if (diff < 0){
                    stack.pop()
                }
                // this means the left asteroid overtakes the right, so we can just break and don't
                // add the current asteroid
                else if (diff > 0){
                    exploded = true
                    break
                }
            }
            // note that if the right asteroid fully overtook the left asteroids,
            // or it was a positive value asteroid to begin with, we just add it on
            if (!exploded){
                stack.push(asteroids[i])
            }
        }
        return stack
    }
}
