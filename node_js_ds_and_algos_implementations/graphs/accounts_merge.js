class Solution {
    /**
     * @param {string[][]} accounts
     * @return {string[][]}
     */
    accountsMerge(accounts) {
        /*
        7/2/2026
        create an adjacency list to determine if emails are connected
        it's a bi-directional graph, so add both directions
        neet@gmail.com: [bob@gmail.com, neet_dsa@gmail.com] 
        alice@gmail.com: []
        neetcode@gmail.com: []
        neet_dsa@gmail.com: [neet@gmail.com]
        bob@gmail.com: [neet@gmail.com]

        for example, if you ran DFS starting at bob@gmail.com, the first edge is
        neet@gmail.com, and then looking at neet@gmail.com's neighbors,
        it'd be bob@gmail.com (which we already saw), and neet_dsa@gmail.com

        so along this path, these emails are all connected, and you can see that
        "neet" is attached to all these emails

        for example, if we ran DFS starting from "neet"
        neet@gmail.com -> bob@gmail.com
                       -> neet_dsa@gmail.com
        
        if we track a set of all the emails we saw, we'd get neet@gmail.com ,bob@gmail.com
        and neet_dsa@gmail.com

        need a separate hashmap that maps an email to a name, its okay if the name gets overwritten
        since its guaranteed that an email always maps to one name and not multiple.

        Include both a global visited set to make sure we don't re-run the DFS on the same email path
        but also a local "visited" that captures the sequence of emails that are connected
        */

        let sortingKey = (a,b) => {
            if (a < b){
                return -1
            }
            if (a > b){
                return 1
            }
            return 0
        }

        let adjacency = {}
        let names = {}
        for (let i = 0; i < accounts.length; ++i){
            // first email in each list is the key for the adjacency list
            if (!(accounts[i][1] in names)){
                // map the email to its name
                names[accounts[i][1]] = accounts[i][0]
            }
            if (!(accounts[i][1] in adjacency)){
                adjacency[accounts[i][1]] = []
            }
            for (let j = 2; j < accounts[i].length; ++j){
                adjacency[accounts[i][1]].push(accounts[i][j])
                if (!(accounts[i][j] in adjacency)){
                    adjacency[accounts[i][j]] = [accounts[i][1]]
                }
                else {
                    adjacency[accounts[i][j]].push(accounts[i][1])
                }

                // map email to the name 
                if (!(accounts[i][j] in names)){
                    names[accounts[i][j]] = accounts[i][0]
                }
            }
        }

        let visited = new Set()
        let globalVisited = new Set()
        const dfs = (email, visited) => {
            if (visited.has(email)){
                return
            }
            visited.add(email)
            globalVisited.add(email)
            for (let neighbor of adjacency[email]){
                dfs(neighbor, visited)
            }
        }

        // run dfs on each email
        let res = []
        for (let email of Object.keys(names)){
            if (!globalVisited.has(email)){
                visited = new Set()
                dfs(email, visited)
                let emails = [...visited]
                let correspondingName = names[emails[0]]
                emails.sort(sortingKey)
                res.push([correspondingName, ...emails])
            }
        }
        return res
    }
}
