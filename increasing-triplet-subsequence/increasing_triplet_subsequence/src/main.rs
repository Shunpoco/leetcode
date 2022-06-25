struct Solution;
impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let mut dp = vec![];
        for &num in nums.iter() {
            if let Some(v) = dp.binary_search(&num).err() {
                if v >= dp.len() {
                    dp.push(num);
                } else {
                    dp[v] = num;
                }                
            }
        }
        
        // println!("{:?}", dp);
        
        dp.len() >= 3
    }
}

fn main() {
    assert_eq!(Solution::increasing_triplet(vec![2,1,5,0,4,6]), true);
}
