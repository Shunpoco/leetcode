struct Solution {}

impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let s = format!("{:b}", n);
                
        let char_vec: Vec<char> = s.chars().collect();
        
        let mut one_count = 0usize;
        for c in char_vec {
            if c == '1' {
                one_count += 1;
            }
        }
        
        one_count == 1        
    }
}

fn main() {
    println!("{:?}", Solution::is_power_of_two(2));
}
