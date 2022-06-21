/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = nums => {
    return (nums.map((sum => value => sum += value)(0)))
    
};