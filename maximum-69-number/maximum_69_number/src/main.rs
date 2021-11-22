struct Solution {}

impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        let mut digit = -1i32;
        let mut n = num;
        
        let mut i = 0i32;
        while n != 0 {
            if n % 10 == 6 {
                digit = i;
            }
            n = n / 10;
            i += 1;
        }
        
        if digit == -1 {
            return num;
        }
        num + 3 * i32::pow(10, digit as u32)
    }
}

fn main() {
    assert_eq!(Solution::maximum69_number(6696), 9696);
}
