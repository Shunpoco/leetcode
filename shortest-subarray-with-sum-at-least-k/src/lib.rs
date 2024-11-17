use std::collections::VecDeque;
struct Solution;
impl Solution {
    pub fn shortest_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as i64;
        let n = nums.len();

        let mut cums = vec![0; n+1];

        for i in 1..n+1 {
            cums[i] = cums[i-1] + (nums[i-1] as i64);
        }

        let mut deque = VecDeque::new();
        let mut result = -1;

        for i in 0..n+1 {
            while deque.len() > 0 && cums[i] - cums[deque[0]] >= k {
                result = if result == -1 || result > ((i - deque[0]) as i32) {
                    let v = deque.pop_front().unwrap();
                    (i - v) as i32
                } else {
                    deque.pop_front().unwrap();
                    result
                };
            }

            while deque.len() > 0 && cums[i] <= cums[deque[deque.len()-1]] {
                deque.pop_back().unwrap();
            }

            deque.push_back(i);
        }

        result
    }
}



#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn case1() {
        let nums = vec![1];
        let k = 1;

        let got = Solution::shortest_subarray(nums, k);

        assert_eq!(got, 1);
    }

    #[test]
    fn case2() {
        let nums = vec![1, 2];
        let k = 4;

        let got = Solution::shortest_subarray(nums, k);

        assert_eq!(got, -1);
    }

    #[test]
    fn case3() {
        let nums = vec![2, -1, 2];
        let k = 3;

        let got = Solution::shortest_subarray(nums, k);

        assert_eq!(got, 3);
    }

    #[test]
    fn case4() {
        let nums = vec![77,19,35,10,-14];
        let k = 19;

        let got = Solution::shortest_subarray(nums, k);

        assert_eq!(got, 1);
    }
}
