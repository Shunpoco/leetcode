struct Solution {}

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut result = 0i32;
        let mut current = 0i32;

        for p in gain {
            current += p;
            
            if result < current {
                result = current;
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::largest_altitude(vec![-5,1,5,0,-7]), 1);
}
