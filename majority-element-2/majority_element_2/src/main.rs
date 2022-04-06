struct Solution;
impl Solution {
    pub fn majority_element(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        
        nums.sort();
        let mut result = vec![];
        
        let mut cur = i32::MAX;
        let mut cc = 0usize;
        for &num in nums.iter() {
            if cur != num {
                if 3*cc > n {
                    result.push(cur);
                }
                cur = num;
                cc = 0;
            }
            cc += 1;
        }
        if 3*cc > n {
            result.push(cur);
        }
        result
    }
}

fn main() {
    assert_eq!(Solution::majority_element(vec![1,2,1,1]), vec![1]);
}
