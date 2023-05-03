struct Solution;
impl Solution {
    pub fn find_difference(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result1 = vec![];
        let mut result2 = vec![];

        nums1.sort();
        nums2.sort();
        let mut prev1 = 1001;
        let mut prev2 = 1001;
        while nums1.len() > 0 && nums2.len() > 0 {
            let v1 = nums1[nums1.len()-1];
            let v2 = nums2[nums2.len()-1];
            if prev1 == v1 {
                nums1.pop().unwrap();
                continue;
            }
            if prev2 == v2 {
                nums2.pop().unwrap();
                continue;
            }

            if v1 == v2 {
                prev1 = v1;
                prev2 = v2;
                nums1.pop().unwrap();
                nums2.pop().unwrap();
            } else if v1 > v2 {
                prev1 = v1;
                result1.push(v1);
                nums1.pop().unwrap();
            } else {
                prev2 = v2;
                result2.push(v2);
                nums2.pop().unwrap();
            }
        }

        while nums1.len() > 0 {
            let v = nums1[nums1.len()-1];
            if prev1 != v {
                result1.push(v);
                prev1 = v;
            }
            nums1.pop().unwrap();
        }

        while nums2.len() > 0 {
            let v = nums2[nums2.len()-1];
            if prev2 != v {
                result2.push(v);
                prev2 = v;
            }
            nums2.pop().unwrap();
        }


        vec![result1, result2]
    }
}

fn main() {
    let v1 = vec![1,2,3];
    let v2 = vec![2,4,6];
    println!("{:?}", Solution::find_difference(v1, v2));
}
