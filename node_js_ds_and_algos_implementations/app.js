// entry point for the node.js application
const Queue = require("./Queue").Queue

console.log("***************** Running Queue Test ****************")

q = new Queue()
q.push(1)
q.push(2)
q.push(3)
q.pop()
console.log(q.peek())
q.pop()
q.pop()
console.log(q.isEmpty())
