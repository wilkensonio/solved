class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        int preIndex = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = preIndex;
            preIndex *= nums[i];
        }

        int posIndex = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= posIndex;
            posIndex *= nums[i];
        }

        return result;
    }

}

/*
 * public int[] productExceptSelf(int[] nums) {
 * int len = nums.length;
 * int[] result = new int[len];
 * Arrays.fill(result, 1);
 * 
 * int preI = 1;
 * int postI = 1;
 * int i = 0;
 * 
 * while (len > i) {
 * result[i] *= preI;
 * preI *= nums[i];
 * result[len - i - 1] *= postI;
 * postI *= nums[len - i -1];
 * i++;
 * }
 * 
 * 
 * return result;
 * }
 */