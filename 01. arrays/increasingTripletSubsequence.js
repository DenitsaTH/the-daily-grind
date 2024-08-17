/*Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.*/


var increasingTriplet = function (nums) {
    let curr_min1 = Infinity;
    let curr_min2 = Infinity;

    for (let i = 0; i < nums.length; i++) {

        if (nums[i] <= curr_min1) {
            curr_min1 = nums[i];

        } else if (nums[i] <= curr_min2) {
            curr_min2 = nums[i];

        } else {
            return true;
        }
    }

    return false;
};