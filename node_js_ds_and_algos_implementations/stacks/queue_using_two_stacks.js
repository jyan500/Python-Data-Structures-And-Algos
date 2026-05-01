class MyQueue {
    constructor() {
        /*
        because queues are first in first out, and stacks are last in first out,
        normally if you're just inserting into a stack
        [1,0,2,3], in a stack, you'd pop out 3. But in a queue, 1 would be popped out instead,
        since 1 was inserted first

        if the stack was inserted in reverse order, then the top of the stack also becomes the top of the queue
        [1] insert into stack2 in reverse order
        [1,0,2] now if we wanted to pop
        [2,0,1], and then pop out 1
        overwrite the values of stack 1 in reverse order, [0, 2]
    
        Time: (Brute force solution)
        O(N) pop and peek
        O(1) push and empty

        */
        this.stack1 = []
        this.stack2 = []
    }

    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        this.stack1.push(x)
    }

    /**
     * @return {number}
     */
    pop() {
        this.stack2 = []
        // push everything into stack 2 in reverse order, so now the 
        // top of the "stack" is also the top of the queue
        while (this.stack1.length){
            this.stack2.push(this.stack1.pop())
        }
        // pop out to get the proper top value
        let res = this.stack2.pop()
        // push everything back into stack 1 in reverse order, so now
        // it's back to the original ordering of the stack
        while (this.stack2.length){
            this.stack1.push(this.stack2.pop())
        }
        return res
    }

    /**
     * @return {number}
     */
    peek() {
        this.stack2 = []
        // push everything into stack 2 in reverse order, so now the 
        // top of the "stack" is also the top of the queue
        while (this.stack1.length){
            this.stack2.push(this.stack1.pop())
        }
        // pop out to get the proper top value
        let res = this.stack2[this.stack2.length-1]
        // push everything back into stack 1 in reverse order, so now
        // it's back to the original ordering of the stack
        while (this.stack2.length){
            this.stack1.push(this.stack2.pop())
        }
        return res
        
    }

    /**
     * @return {boolean}
     */
    empty() {
        return this.stack1.length === 0
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
