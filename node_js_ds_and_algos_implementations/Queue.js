/**
 * Queue implementation
 *
 */
class Queue {
	constructor() {
		this.q = []
		this.frontIndex = 0
		this.backIndex = 0
	}
	push(element) {
		this.q.push(element)
		++this.backIndex
	}
	pop() {
		if (!this.isEmpty()){
			let element = this.q[this.frontIndex]
			// note this leaves a null element at the former index,
			// so you need to increment frontIndex by 1
			delete this.q[this.frontIndex]
			++this.frontIndex
			return element
		}
	}
	peek(){
		if (!this.isEmpty()){
			return this.q[this.frontIndex]
		}
		else {
			return -1
		}
	}
	isEmpty(){
		return this.frontIndex === this.backIndex
	}
}

module.exports = { Queue }
