struct Solution;
impl Solution {
    pub fn min_end(n: i32, x: i32) -> i64 {
        let mut n = n as i64;
        let x = x as i64;

        let mut result = x;
        n -= 1;
        let mut m= 1;

        while n > 0 {
            if (m & x) == 0 {
                result |= (n & 1) * m;
                n >>= 1;
            }

            m <<= 1;
        }

        result
    }
}

fn main() {
    let result = Solution::min_end(3, 4);

    assert!(result == 6);

    println!("{}", result);
}
