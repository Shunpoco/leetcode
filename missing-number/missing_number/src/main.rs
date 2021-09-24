struct Solution {}

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let l = nums.len();
        
        let mut res = 0i32;
        for i in 1..l+1 {
            res += i as i32;
        }
        
        for num in nums {
            res -= num;
        }
        
        res
    }
}


fn main() {
    assert_eq!(Solution::missing_number(vec![1,2]), 0);
}

#[test]
fn test_missing_number() {
    assert_eq!(Solution::missing_number(vec![0,1,2]), 3);
}
