struct Solution;
impl Solution {
    pub fn count_quadruplets(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut result = 0;
        
        for i in 0..n-3 {
            for j in i+1..n-2 {
                for k in j+1..n-1 {
                    for l in k+1..n {
                        if nums[l] == nums[i]+nums[j]+nums[k] {
                            result += 1;
                        }
                    }
                }
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::count_quadruplets(vec![1,1,1,3,5]), 4);
}
