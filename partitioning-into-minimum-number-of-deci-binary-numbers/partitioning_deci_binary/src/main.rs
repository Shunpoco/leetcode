struct Solution {}

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
//         let n:Vec<char> = n.chars().collect();
//         let mut m = 0i32;
        
//         for c in n {
//             let v = c as i32 - 48; // in utf-8, '0' is 48.
            
//             if v > m {
//                 m = v;
//             }
//         }
        
//         m
        let m = n.chars().max().unwrap();  
        (m as i32) - 48
    }
}

fn main() {
    assert_eq!(Solution::min_partitions("32".to_string()), 3)
}
