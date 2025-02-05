struct Solution;
impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let mut count = vec![0;26];
        let mut diff = 0;

        let a1 = Vec::from(s1);
        let a2 = Vec::from(s2);

        for (c1, c2) in a1.iter().zip(a2.iter()) {
            count[(c1-97) as usize] += 1;
            count[(c2-97) as usize] -= 1;

            if c1 != c2 {
                diff += 1;
            }
        }

        for &c in count.iter() {
            if c != 0 {
                return false;
            }
        }
        
        diff == 0 || diff == 2
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one() {
        let s1 = String::from("bank");
        let s2 = String::from("kanb");

        let result = Solution::are_almost_equal(s1, s2);

        assert!(result);
    }

    #[test]
    fn two() {
        let s1 = String::from("attack");
        let s2 = String::from("defend");

        let result = Solution::are_almost_equal(s1, s2);

        assert!(!result);
    }

    #[test]
    fn three() {
        let s1 = String::from("kelb");
        let s2 = String::from("kelb");

        let result = Solution::are_almost_equal(s1, s2);

        assert!(result);
    }

    #[test]
    fn four() {
        let s1 = String::from("abcd");
        let s2 = String::from("dcba");

        let result = Solution::are_almost_equal(s1, s2);

        assert!(!result);
    }
}
