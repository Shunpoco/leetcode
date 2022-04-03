struct Solution;
impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        if nums.len() < 2 {
            return;
        }
        
        let min = nums.len()-1;
        let mut max = nums.len()-1;
        let mut i = nums.len()-2;
        let mut swap = false;
        
        loop {
            if nums[min] > nums[i] {
                let t = nums[min];
                nums[min] = nums[i];
                nums[i] = t;
                swap = true;
                break;
            } else if nums[max] > nums[i] {
                let v = &mut nums[max..];
                v.sort();
                for j in max..(min+1) {
                    if nums[j] > nums[i] {
                        let t = nums[j];
                        nums[j] = nums[i];
                        nums[i] = t;
                        break;
                    }
                }
                swap = true;
                println!("{:?}", nums);
                break;
            }

            
            if nums[i] > nums[max] {
                max = i;
            }
            
            if i > 0 {
                i -= 1;            
            } else {
                break;
            }
        }
    
        let v: &mut [i32];
        if swap {
            v = &mut nums[i+1..];
        } else {
            v = &mut nums[..];
        }
        v.sort();
    }
}

fn main() {
    let mut v = vec![1,3,2];
    Solution::next_permutation(&mut v);
    assert_eq!(v, vec![2,1,3]);
}
