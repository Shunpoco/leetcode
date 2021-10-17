struct Solution {}

impl Solution {
    pub fn number_of_steps(num: i32) -> i32 {
        let mut result = 0i32;
        if num == 0 {
            return result;
        }
        result += 1;
        
        let mut new_num = num - 1;
        
        if num % 2 == 0 {
            new_num = num / 2;
        }
        
        result += Solution::number_of_steps(new_num);
        
        result
    }
}

fn main() {
    assert_eq!(Solution::number_of_steps(14), 6);
}
