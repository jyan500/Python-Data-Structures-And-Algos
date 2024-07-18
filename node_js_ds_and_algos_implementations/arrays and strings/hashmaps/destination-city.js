/**
 * @param {string[][]} paths
 * @return {string}
 */
/*
Approach:
Similar to graph problems, you create the adjacency list,
where the key is the src and the value is the list of dst
but also keep track of a set of all cities that are encountered (whether src or dst)

At the end, the city that doesn't have an outgoing edges will NOT be present as a 
src in the adjacency list

paths = [["B", "C"], ["D", "B"], ["C", "A"]]

adjacency = {
    "B": ["C"],
    "D": ["B"],
    "C": ["A"],
}
all Cities = {"A", "B", "C", "D"}
here, "A" is not a src, since it's not present in allCities set, 
so it has no path to another city

Time: O(N)
Space: O(N)
*/
var destCity = function(paths) {
    let adjacency = {}
    let allCities = new Set()
    
    for (let [src, dst] of paths){
        if (!(src in adjacency)){
            adjacency[src] = []
        }
        adjacency[src].push(dst)
        allCities.add(src)
        allCities.add(dst)
    }
    return [...allCities].find(((city) => !(city in adjacency)))
    
};