class Solution {
    /**
     * @param {string} senate
     * @return {string}
     */
    predictPartyVictory(senate) {
        /*
        RRDDD string are all the senators
        each senator can ban one other senator from voting
        if one more senators haven't been banned + are all the same party (i.e all R or all D),
        the round can end.

        the voting round goes from left to right, and then wraps back around until
        a result is found

        RRDDD

        first R takes the rights of the first D (at index 2)
        RR()DD
        second R takes the rights of the second D (at index 3)
        RR( )D
        the next two D's have lost their rights, so skip them
        the last D takes the rights of the first R (index 0)
        ()R( )D
        the last R takes the rights of the last D (index 4)
        ()R(  )
        only R is left

        Greedy approach, 
        the opposing parties should aim to take each other out, so we need to know exactly where the 
        opposing party's indexes are located in the string beforehand using hashmap

        Flaw in my current greedy approach (prompted claude to help me out here when i was failing this test case):
        senate="DRRDRDRDRDDRDRDR"
        I'm currently always picking the first possible senate using the "shift()" function to pop
        out from that candidate pool, but i'm not considering whether that candidate actually voted or not
        this round.
        
        From a strategic standpoint, it's better to pick a candidate from the opposing party that 
        hasn't voted yet, so they lose their voting power this round. So rather than using shift(),
        you'd need to pick a candidate in the opposing pool that has an index > the current index

        O(N^2), since we have to continually scan the list to find the next opposing candidate
        O(N) space for the hashmap

        */
        let map = {"R": [], "D": []}
        for (let i = 0; i < senate.length; ++i){
            map[senate[i]].push(i)
        }
        // track a set to show who's been banned
        let banned = new Set()
        let k = 0
        while (true){
            if (map["R"].length === 0 && map["D"].length !== 0){
                return "Dire"
            }
            else if (map["R"].length > 0 && map["D"].length === 0){
                return "Radiant"
            }
            // use mod so that the indices will wrap around back to the beginning
            // after it's reached the end of the array
            let index = k % senate.length
            // if this senate hasn't been banned
            if (!(banned.has(index))){
                if (senate[index] === "D"){
                    if (map["R"].length){
                        // find the first senate of the opposing party that hasn't voted yet (i > k)
                        let bannedIndex = map["R"].filter((i) => i > k)[0]
                        // if there is no senator of the opposing party that goes after the current person
                        // just wrap around pick the first senator of the opposing party that appears
                        if (!bannedIndex){
                            // just pick the first one in the list
                            bannedIndex = map["R"][0]
                        }
                        // remove the element from the map
                        map["R"].splice(map["R"].indexOf(bannedIndex), 1)
                        banned.add(bannedIndex)
                    }
                }
                else {
                    if (map["D"].length){
                        let bannedIndex = map["D"].filter((i) => i > k)[0]
                        if (!bannedIndex){
                            bannedIndex = map["D"][0]
                        }
                        map["D"].splice(map["D"].indexOf(bannedIndex), 1)
                        banned.add(bannedIndex)
                    }
                }
            }
            k++
        }
    }
}
