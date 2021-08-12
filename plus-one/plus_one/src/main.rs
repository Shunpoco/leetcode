struct Solution {}

impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut res = digits;
        let mut carry = 1i32;
        let mut idx = res.len();
        
        while idx > 0 {
            idx -= 1;
            let mut v = res[idx] + carry;
            if v > 9 {
                v = 0;
            } else {
                carry = 0;
            }
            
            res[idx] = v;
            
            if carry == 0 {
                break;
            }
        }
        
        if idx == 0 && carry == 1 {
            res.insert(0, 1);
        }
        
        res
    }
}

fn main() {
    let v = Solution::plus_one(vec![9,9,9]);
    println!("{:?}", v);
}

#[test]
fn test_plus_one() {
    assert_eq!(Solution::plus_one(vec![1,2,3]), vec![1,2,4]);
    assert_eq!(Solution::plus_one(vec![9,9,9]), vec![1,0,0,0]);
}