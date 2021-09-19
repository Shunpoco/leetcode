struct Solution {}

// use string
// impl Solution {
//     pub fn is_power_of_two(n: i32) -> bool {
//         if n <= 0 {
//             return false;
//         }
//         let s = format!("{:b}", n);
                
//         let char_vec: Vec<char> = s.chars().collect();
        
//         let mut one_count = 0usize;
//         for c in char_vec {
//             if c == '1' {
//                 one_count += 1;
//             }
//         }
        
//         one_count == 1        
//     }
// }

// use bit manipulation
impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 { return false; }
        
        let mut n = n;
        let mut count_one = 0usize;
        
        while n > 0 {
            if n & 1 == 1 {
                count_one += 1;
                if count_one > 1 { return false; }         
            }
            n = n >> 1;
        }
        true
    }
}

fn main() {
    println!("{:?}", Solution::is_power_of_two(2));
}
