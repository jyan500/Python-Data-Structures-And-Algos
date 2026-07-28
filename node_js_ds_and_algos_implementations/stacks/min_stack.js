class MinStack {
    constructor() {
        /* 
        Revisited 7/26/2026
        (slightly different logic for pushing onto the min stack but the same outcome)
        you want to use 2 stacks
        one of them only stores the absolute min at each moment,
        so the moment we find a min that's smaller, than we add to that stack
        If it's not smaller, we don't add it
        That way, we know the absolute min at any point,
        as well as the actual ordering of the elements for normal push/pop functions

        The only question is that how do we know we've removed all instances of an element?
        so that it can be removed from the min stack?

        Actually refining the top rule above, if we push to the min stack if its <= min (rather
        than strictly smaller), we can also track the potential duplicates, so that way when popping,
        if top of the regular stack == top of min stack, we pop from both

        Pop/top/getmin will always be called on non-empty stacks, so don't need to add the checks there,
        otherwise, you'd just check the length before performing any of these functions

        */
        this.minStack = []
        this.stack = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        if (this.minStack.length > 0){
            if (val <= this.minStack[this.minStack.length-1]){
                this.minStack.push(val)
            }
            this.stack.push(val)
        }
        else {
            this.minStack.push(val)
            this.stack.push(val)
        }
    }

    /**
     * @return {void}
     */
    pop() {
        if (this.stack[this.stack.length-1] === this.minStack[this.minStack.length-1]){
            this.minStack.pop()
        }
        this.stack.pop()
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length-1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack[this.minStack.length-1]
    }
}

var MinStack = function() {
    this.stack = []
    // the min stack always keeps track of the current minimum element
    // at the time of a push/pop operation
    // so if the value that's being pushed/popped is not less than min,
    // we just push the existing min value onto the stack again.
    // this way, the min will always be at the top of the stack, even if it's 
    // value has not changed during a given push/pop operation
    this.minStack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    if (this.minStack.length > 0){
        if (this.minStack[this.minStack.length-1] < val){ 
            this.minStack.push(this.minStack[this.minStack.length-1])
        }
        else {
            this.minStack.push(val)
        }
    }
    else {
       this.minStack.push(val)  
    }
    this.stack.push(val) 
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if (this.stack.length > 0){
        this.minStack.pop()
        return this.stack.pop()
    }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    if (this.stack.length > 0){
        return this.stack[this.stack.length-1]
    }
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minStack[this.minStack.length-1]
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */