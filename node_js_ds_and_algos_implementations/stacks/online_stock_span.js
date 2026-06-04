class StockSpanner {
    constructor() {
        /*
        stack problem (similar to daily temperatures)
        brute force way is to iterate backwards until you see a number that's greater than
        the current.
        however, the bottleneck is that every time we want the current span,
        we have to loop all the way back until we find an element greater than the price,
        however, recalling from daily temperatures, you store both the price,
        and the span within the stack, when a new price arrives,
        compare the top price to the current price, 
        if the top price <= currentPrice,
        pop out the top price, add its span to the current span,
        since the span basically stops at top price (because current price > top price)

        StockSpanner","next","next","next","next","next","next","next"]
        [[],[100],[80],[60],[70],[60],[75],[85]]

        in the following example:
        [[100, 1], [80, 1], [60, 1]]
        however at 70, because 60 is less than 70,
        [[100,1],[80,1],[70,2]]
        we pop out 60, and add it to the span, which gives the result [70,2]
        [[100,1],[80,1],[70,2],[60,1]]
        at 75,
        [[100,1],[80,1],[70,2],[60,1]
        we pop out 60, then 70, and add their spans,
        since these are both less than 75
        [[100,1],[80,1],[75,4]]

        */
        this.stack = []
    }

    /**
     * @param {number} price
     * @return {number}
     */
    next(price) {
        // need to add it stack
        let res = 1
        while (this.stack.length && price >= this.stack[this.stack.length-1][0]){
            let [topPrice, topSpan] = this.stack.pop()
            res += topSpan
        }
        this.stack.push([price, res])
        return res
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
