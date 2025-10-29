struct Solution;
impl Solution {
    pub fn smallest_number(n: i32) -> i32 {
        let mut v = 1;

        while v < n {
            v = (v << 1) + 1;
        }

        v
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let n = 5;
        let got = Solution::smallest_number(n);

        assert_eq!(got, 7);
    }

    #[test]
    fn second() {
        let n = 10;
        let got = Solution::smallest_number(n);

        assert_eq!(got, 15);
    }

    #[test]
    fn third() {
        let n = 3;
        let got = Solution::smallest_number(n);

        assert_eq!(got, 3);
    }
}
