struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut v: Vec<Vec<char>> = vec![];
        
        let mut shortest = 201;
        
        for i in 0..strs.len() {
            let cs:Vec<char> = strs[i].chars().collect::<Vec<char>>().clone();
            let l = cs.len();
            v.push(cs);
            if l < shortest {
                shortest = l;
            }
        }

        let mut last_idx = 0usize;
        
        for i in 0..shortest {
            let c = v[0][i];
            for j in 1..v.len() {
                if c != v[j][i] {
                    return strs[0][0..last_idx].to_string();
                }
            }
            last_idx += 1;
        }
        
        return strs[0][0..last_idx].to_string()
    }
}

fn main() {
    assert_eq!(Solution::longest_common_prefix(vec!["flower".to_string(), "fl".to_string()]), "fl".to_string());
}

#[test]
fn test_longest_common_prefix() {
    assert_eq!(Solution::longest_common_prefix(vec!["flower".to_string(),"flow".to_string(),"flight".to_string()]), "fl".to_string());
    assert_eq!(Solution::longest_common_prefix(vec!["dog".to_string(),"racecar".to_string(),"car".to_string()]), "".to_string());
}
