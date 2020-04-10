/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    nums = nums.sort(function (a, b) { return a - b; });
    let largest = nums.slice(-1)[0];
    for (let k = nums.length - 2; k >= 0; k--) {
        if (largest !== nums[k]) return nums[k];
    }
    return largest;
}

