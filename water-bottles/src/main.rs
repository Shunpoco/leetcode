struct Solution;
impl Solution {
    pub fn num_water_bottles(mut num_bottles: i32, num_exchange: i32) -> i32 {
        let mut result = 0;
        let mut left_over = 0;

        while num_bottles > 0 {
            result += num_bottles;

            left_over += num_bottles;
            num_bottles = left_over / num_exchange;
            left_over -= left_over / num_exchange * num_exchange;
        }

        result
    }
}

fn main() {
    let num_bottles = 15;
    let num_exchange = 4;

    let got = Solution::num_water_bottles(num_bottles, num_exchange);
    
    assert!(got == 19);

    println!("{}", got);
}
