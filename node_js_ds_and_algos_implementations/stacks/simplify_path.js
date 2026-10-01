class Solution {
    /**
     * @param {string} path
     * @return {string}
     */
    simplifyPath(path) {
        /* 
        1) Split by "/", since any amount of slashes should simplify down to a "" since
        it's the common delimiter here,
        remove the ""
        2) Use stack to push elements, and then pop out the top if the current is "..", or don't push onto the stack if its "."
        3) re-join the elements together with "/" and add initial "/" for the root

        Time: O(N)
        Space: O(N)
        */
        let parts = path.split("/").filter(str => str !== "")
        let stack = []
        for (let i = 0; i < parts.length; ++i){
            if (stack.length > 0){
                // ".." means previous directory, so pop out the top of the stack
                if (parts[i] === ".."){
                    stack.pop()
                    continue
                }
                // if single period, this represents the current directory,
                // no need to add anything
                if (parts[i] === "."){
                   continue 
                }
                stack.push(parts[i])
            }
            else {
                if (parts[i] !== ".." && parts[i] !== "."){
                    stack.push(parts[i])
                }
            }
        }
        // always needs the initial "/" for the root directory, which is
        // removed during the initial parsing
        return "/" + stack.join("/")
    }
}
