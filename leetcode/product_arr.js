let productExceptSelf = function (nums) {
    let len = nums.length;
    let result = new Array(len).fill(1);
    let preI = 1;
    let postI = 1;
    let i = 0;

    while (len > i) {
        result[i] *= preI;
        preI *= nums[i];
        result[len - i - 1] *= postI;
        postI *= nums[len - i - 1];
        i++;
    }
    return result;
}
console.log(productExceptSelf([1, 2, 3, 4]));
