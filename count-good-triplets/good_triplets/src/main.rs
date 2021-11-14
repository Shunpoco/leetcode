struct Solution {}

impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let l = arr.len();
        let mut result = 0i32;
        
        
        for i in 0..(l-2) {
            for j in (i+1)..(l-1) {
                for k in (j+1)..l {
                    let (v1, v2, v3) = (arr[i], arr[j], arr[k]);
                    if Solution::abs(v1, v2) <= a && Solution::abs(v2, v3) <= b && Solution::abs(v1, v3) <= c {
                        result += 1;
                    }
                }
            }
        }
        
        result
    }
    
    fn abs(a: i32, b: i32) -> i32 {
        let mut v = a - b;
        if v < 0 {
            v *= -1;
        }
        
        v
    }
}


fn main() {
    assert_eq!(Solution::count_good_triplets(vec![3,0,1,1,9,7], 7, 2, 3), 4);
}
