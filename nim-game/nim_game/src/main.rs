struct Solution;
impl Solution {
    pub fn can_win_nim(n: i32) -> bool {
        if n % 4 == 0 { false } else { true }
    }
}

fn main() {
    assert_eq!(Solution::can_win_nim(7), true);
}
