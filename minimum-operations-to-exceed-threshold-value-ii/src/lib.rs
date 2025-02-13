use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut result = 0;
        let mut bh = BinaryHeap::new();

        for num in nums {
            bh.push(-num as i64);
        }

        while *bh.peek().unwrap() > (-k as i64) {
            let v1 = -bh.pop().unwrap();
            let v2 = -bh.pop().unwrap();

            let t = v1.min(v2) * 2 + v1.max(v2);

            bh.push(-t);
            result += 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let nums = vec![2, 11, 10, 1, 3];
        let k = 10;

        let got = Solution::min_operations(nums, k);

        assert_eq!(2, got);
    }

    #[test]
    fn second() {
        let nums = vec![1, 1, 2, 4, 9];
        let k = 20;

        let got = Solution::min_operations(nums, k);

        assert_eq!(4, got);
    }

    #[test]
    fn third() {
        let nums = vec![999999999, 999999999, 999999999];
        let k = 1000000000;

        let got = Solution::min_operations(nums, k);

        assert_eq!(2, got);
    }
}
