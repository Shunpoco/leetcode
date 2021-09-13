struct Solution {}

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let (mut m, mut n) = (m as usize, n as usize);
        
        while n > 0 {
            if m > 0 && nums1[m-1] > nums2[n-1] {
                nums1[m+n-1] = nums1[m-1];
                m -= 1;
            } else {
                nums1[m+n-1] = nums2[n-1];
                n -= 1;
            }
        }
    }
}

fn main() {
    let mut a = vec![1,2,3,0,0,0];
    let mut b = vec![2,5,6];

    let len_a = a.len() - b.len();
    let len_b = b.len();

    Solution::merge(&mut a, len_a as i32, &mut b, len_b as i32);

    println!("{:?}", a);
}
