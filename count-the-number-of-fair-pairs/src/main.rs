struct Solution;
impl Solution {
    pub fn count_fair_pairs(mut nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        nums.sort();

        let n = nums.len();

        let mut result = 0;
        for i in 0..n {
            let low = Solution::search_bound(&nums, i+1, n-1, lower-nums[i]);
            let high = Solution::search_bound(&nums, i+1, n-1, upper-nums[i]+1);

            result += (high - low) as i64;
        }

        result
    }

    fn search_bound(nums: &Vec<i32>, mut low: usize, mut high: usize, target: i32) -> usize {
        while low <= high {
            let mid = low + ((high - low) / 2);

            if nums[mid] >= target {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        low
    }
}

fn main() {
    let nums = vec![0,1,7,4,4,5];
    let lower = 3;
    let upper = 6;

    let got = Solution::count_fair_pairs(nums, lower, upper);

    print!("{}", got);
    assert!(got == 6);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_case() {
        let nums = vec![0, 1, 7, 4, 4, 5];
        let lower = 3;
        let upper = 6;
        assert_eq!(Solution::count_fair_pairs(nums, lower, upper), 6);
    }

    #[test]
    fn test_no_pairs() {
        let nums = vec![10, 20, 30];
        let lower = 1;
        let upper = 5;
        assert_eq!(Solution::count_fair_pairs(nums, lower, upper), 0);
    }

    #[test]
    fn test_all_pairs() {
        let nums = vec![1, 1, 1, 1];
        let lower = 2;
        let upper = 2;
        assert_eq!(Solution::count_fair_pairs(nums, lower, upper), 6);
    }

    #[test]
    fn test_large_range() {
        let nums = vec![1, 2, 3, 4, 5];
        let lower = 0;
        let upper = 10;
        assert_eq!(Solution::count_fair_pairs(nums, lower, upper), 10);
    }

    #[test]
    fn test_single_element() {
        let nums = vec![1];
        let lower = 1;
        let upper = 2;
        assert_eq!(Solution::count_fair_pairs(nums, lower, upper), 0);
    }
}

