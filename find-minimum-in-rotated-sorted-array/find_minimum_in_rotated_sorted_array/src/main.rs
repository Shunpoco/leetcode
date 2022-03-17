struct Solution;
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut l = 0usize;
        let mut r = nums.len()-1;
        
        while l < r {
            let m = (l+r)/2;
            
            if nums[m] < nums[m+1] {
                if nums[l] < nums[m] && nums[m] < nums[r] {
                    l = 0;
                    r = 0;
                } else if nums[l] < nums[m] && nums[m] > nums[r] {
                    l = m+1;
                } else {
                    r = m;
                }
            } else {
                l = m+1;
                r = m+1;
            }
        }
        
        nums[l]
    }
}

fn main() {
    assert_eq!(Solution::find_min(vec![4,5,6,7,0,1,1]), 0);
}
