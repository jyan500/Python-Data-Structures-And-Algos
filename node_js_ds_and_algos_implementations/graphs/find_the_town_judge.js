class Solution {
    /**
     * @param {number} n
     * @param {number[][]} trust
     * @return {number}
     */
    findJudge(n, trust) {
        /*
        2/18/2026
        A -> B means A trusts B
        so if every other person trusts the town judge

        A => B <- C

        that means every other element will have an edge in the adjacency list
        except one element, so the answer is just the node that doesn't have any
        incoming edges 

        every node besides the town judge must point at the town judge as well
        */
        let adjacency = {}
        for (let i = 0; i < n; ++i){
            adjacency[i+1] = []
        }
        for (let [a, b] of trust){
            adjacency[a].push(b)
        }
        let potentialJudge;
        for (let person of Object.keys(adjacency)){
            if (adjacency[person].length === 0){
                potentialJudge = parseInt(person)
                break
            }
        }
        if (potentialJudge){
            for (let person of Object.keys(adjacency)){
                person = parseInt(person)
                // if there's no edge to the town judge, this is also an invalid setup,
                // as every other person (besides the judge) must trust the edge
                if (person !== potentialJudge && !adjacency[person].includes(potentialJudge)){
                    return -1
                }
            }
            return potentialJudge
        }
        return -1
    }
}
