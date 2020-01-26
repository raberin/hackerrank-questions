/*
input: [arr], int(how many times you want to rotate)
output: [rotated arr]

example: 
intput: [1,2,3,4,5], 1 
output: [2,3,4,5,1]

example 2: 
intput: [1,2,3], 1 
output: [3,2,1], 2
*/

// O(n) Iterative - Functional - Non mutating
const rotLeft = (arr, num) => {
    let result = arr
    for(let i = 0; i < num; i++){
        // Remove the first number in arr and push it to end
        result.push(result.shift())
    }
    return result
}