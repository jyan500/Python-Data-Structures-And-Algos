/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    /*
    https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
    Counting Solution
    square students are 1
    circle students are 0
    trickier solution, but one observation to speed up the problem is that
    1) if num(square students) === num(square sandwiches) AND num(circle sandwiches) === num (circle students), everyone can be fed
    2) In the sandwich array, if we encounter a square sandwich, decrement amount of square students
    if encountering a circle sandwich, decrement amount of circle students
    3) If there are no more square sandwiches, and no more square students to eat them, that means
    the rest of the students are circle students, and they can't eat them, therefore, we just return
    the circle student count as the "unfed" students
     same logic applies for the square students
     
    Time Complexity: O(N+M)
    Space: O(1)
    */
    for (let student of students){
        if (student === 1){
            squareStudentCount++
        }
        else {
            circleStudentCount++
        }
    }
    for (let sandwich of sandwiches){
        if (sandwich === 0 && circleStudentCount === 0){
            return squareStudentCount
        }
        else if (sandwich === 1 && squareStudentCount === 0){
            return circleStudentCount
        }
        if (sandwich === 0){
            circleStudentCount--
        }
        else {
            squareStudentCount--
        }
    }
    return 0
    /*
    simulation problem using queues
    
    because there's a chance none of the remaining students want to take the top sandwich, keep track of lastServed variable
    whenever we can't serve the sandwich to the student, increment lastServed
    if we can serve the sandwich however, reset lastServed to 0
    if lastServed is the same length as the amount of students remaining, that means
    we've attempted to serve every student already, so we need to break
    
    lastServed = 0
    while (there are students and sandwiches left)
        if (lastServed === length of students){
            break
        }
        if (top of students array === top of sandwiches array)
            pop from students
            pop from sandwiches
            lastServed = 0
        else
            pop from students
            append students at the end
            lastServed++
    return length of students

    Time: O(N*M), where N is the length of students and M is the length of sandwiches
    it's N*M because at worst, each student can be offered the wrong type of sandwich multiple times,
    so they are pushed to the back of the array M times until they can eat the sandwich and are removed from the queue

    Space: O(N+M)
    */
    let lastServed = 0
    while (students.length && sandwiches.length){
        if (lastServed === students.length){
            break
        }
        if (students[0] === sandwiches[0]){
            // pop from the front of the queue for both sandwich and students queues
            students.shift()
            sandwiches.shift()
            lastServed = 0
        }
        else {
            let student = students.shift()
            // pop from the front and push to the back of the queue
            // since this student cannot eat this sandwich
            students.push(student)
            ++lastServed
        }
    }
    return students.length
};