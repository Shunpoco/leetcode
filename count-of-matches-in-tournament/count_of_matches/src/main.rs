struct Solution {}

impl Solution {
    pub fn number_of_matches(n: i32) -> i32 {
        if n == 1 {
            return 0;
        }
        
        if n % 2 == 0 {
            return n / 2 + Solution::number_of_matches(n/2);
        }
        (n - 1) / 2 + Solution::number_of_matches((n-1)/2+1)
    }
}

fn main() {
    assert_eq!(Solution::number_of_matches(14), 13);
}
