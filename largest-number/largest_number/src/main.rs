use std::cmp::Ordering;

fn comp(a: &str, b: &str) -> Ordering {
    let mut c = String::from(a);
    let mut d = String::from(b);
    
    c.push_str(b);
    d.push_str(a);
    
    if c > d {
        return Ordering::Greater;
    } else if c == d {
        return Ordering::Equal;
    } else {
        return Ordering::Less;
    }
}

struct Solution;
impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut s = vec![];
        for &n in nums.iter() {
            s.push(n.to_string());
        }
        
        s.sort_by(|a, b| comp(&b, &a)); // Descendent
        
        println!("{:?}", s);
        
        if s[0] == "0".to_string() {
            return "0".to_string();
        }
        
        let mut result = "".to_string();
        
        for c in s.iter() {
            result.push_str(c);
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::largest_number(vec![3,30,34,5,9]), "9534330".to_string());
}
