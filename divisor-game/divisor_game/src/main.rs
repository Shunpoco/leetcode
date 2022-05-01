struct Solution;
impl Solution {
    pub fn divisor_game(n: i32) -> bool {
        if n%2 == 0 { true } else { false }
    }
}

fn main() {
    assert_eq!(Solution::divisor_game(10), true);
}
