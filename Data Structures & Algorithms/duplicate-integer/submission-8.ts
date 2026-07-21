class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean} 
     */
    hasDuplicate(nums: number[]): boolean {
        const seen = new Set();
        let i = 0;
        while (i < nums.length) {
            if (seen.has(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
            i++;
        }
        return false;
    }
}
