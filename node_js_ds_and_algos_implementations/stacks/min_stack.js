
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