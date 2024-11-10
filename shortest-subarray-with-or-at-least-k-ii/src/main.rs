struct Solution;
impl Solution {
    pub fn minimum_subarray_length(nums: Vec<i32>, mut k: i32) -> i32 {
        let mut mins = i32::MAX;

        let mut start = 0;
        let mut end = 0;

        let mut bits = Vec::new();
        for i in 0..32 {
            bits.push(0);
        }

        while end < nums.len() {
            Solution::update(&mut bits, nums[end], 1);

            while start <= end && Solution::convert(&bits) >= k {
                mins = std::cmp::min(mins, (end-start+1) as i32);
                Solution::update(&mut bits, nums[start], -1);
                start += 1;
            }
            end += 1;
        }

        if mins == i32::MAX { -1 } else { mins }
    }

    fn convert(bits: &Vec<i32>) -> i32 {
        let mut result = 0;

        for p in 0..32 {
            if (*bits)[p] > 0 {
                result |= 1 << p;
            }
        }

        result
    }

    fn update(bits: &mut Vec<i32>, num: i32, diff: i32) {
        for p in 0..32 {
            if num & (1<<p) > 0 {
                (*bits)[p] += diff
            }
        }
    }
}

fn main() {
    let nums = vec![1,2,3];
    let k = 2;
    let got = Solution::minimum_subarray_length(nums, k);

    assert!(got == 1);

    print!("{}", got);
}
