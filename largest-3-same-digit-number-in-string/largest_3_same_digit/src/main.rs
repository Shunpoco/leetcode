struct Solution;
impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let num:Vec<char> = num.chars().collect();
        
        let mut res = "".to_string();
        let mut cur = vec![];
        for &n in num.iter() {
            if cur.len() == 0 || cur[cur.len()-1] == n {
                cur.push(n);
            } else {
                cur = vec![n];
            }
            
            if cur.len() == 3 {
                let v = cur.iter().collect::<String>();
                if res < v {
                    res = v;
                }
                cur = vec![];
            }
        }
        
        res
    }
}

fn main() {
    assert_eq!(Solution::largest_good_integer("6777133339".to_string()), "777".to_string());
}
