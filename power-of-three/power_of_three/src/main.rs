struct Solution {}

impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
//         if n < 1 {
//             return false;
//         }
        
//         let mut n = n;
        
//         while n > 1 {
//             if n % 3 != 0 {
//                 return false;
//             }
//             n /= 3;
//         }
        
//         true
        n > 0 && 1162261467 % n == 0
    }
}


fn main() {
    assert_eq!(Solution::is_power_of_three(9), true);
}
