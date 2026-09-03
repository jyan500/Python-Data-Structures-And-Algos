class TimeMap {
    constructor() {
        /* 
            use binary search to search the timestamps array for each key
            to find the nearest possible timestamp (assuming the timestamp doesn't exist) 

            map = { "alice": [["happy", 1], ["sad", 3]]} 

            if we search for alice, 2, we should get "happy", since 1 <= 2
            
            note that the way the values are added, it will always be in increasing order,
            so don't need to worry about using a heap to keep it sorted
        */
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if (this.keyStore.get(key) != null){
            this.keyStore.set(key, [...this.keyStore.get(key), [value, timestamp]])
        }
        else {
            this.keyStore.set(key, [[value, timestamp]])
        }
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        if (this.keyStore.get(key)){
            const results = this.keyStore.get(key)
            let l = 0
            let r = results.length - 1
            let resIndex = -1
            while (l <= r){
                let mid = l + Math.floor((r-l)/2)
                let [_, tStamp] = results[mid]
                if (tStamp === timestamp){
                    resIndex = mid
                    break
                }
                // we set the answer here in case this is our actual answer
                // and the timestamp we're looking for doesn't exist,
                // we get the closest possible one that's still less than the actual timestamp
                else if (tStamp < timestamp){
                    resIndex = mid
                    // search right
                    l = mid + 1
                }
                else {
                    r = mid - 1
                }
            }
            // return the string value if we found a timestamp that is smaller
            // than the previous
            return resIndex !== -1 ? results[resIndex][0] : ""
        }
        // if the key doesn't exist, return ""
        return ""
    }
}
