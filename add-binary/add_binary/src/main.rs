struct Solution {}

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut carry: char = '0';
        let mut result: Vec<char> = Vec::new();
        let mut ac = a.chars().rev();
        let mut bc = b.chars().rev();
        
        let mut va: char = '0';
        let mut vb: char = '0';
        let mut isNone = 0usize;

        loop {
            println!("{}", carry);
            match ac.next() {
                Some(v) => va = v,
                None => {
                    va = '0';
                    isNone += 1;
                },
            }
            match bc.next() {
                Some(v) => vb = v,
                None => {
                    vb = '0';
                    isNone += 1;
                },
            }

            if isNone == 2 {
                break;
            }
            let mut v = Self::add(va, vb, carry);
            result.push(v.0);
            carry = v.1;
            isNone = 0;
        }
        
        if carry == '1' {
            result.push(carry);
        }
        
        result.iter().rev().collect::<String>()
    }
    
    fn add(a: char, b: char, c: char) -> (char, char) {
        let mut v = '0';
        let mut carry = '0';
        
        if a == '1' {
            v = '1';
        }
        
        if b == '1' {
            if v == '1' {
                v = '0';
                carry = '1';
            } else {
                v = '1';
            }
        }
        
        if c == '1' {
            if v == '1' {
                v = '0';
                carry = '1';
            } else {
                v = '1';
            }
        }
        
        (v, carry)
    }
}

fn main() {
    Solution::add_binary("01".to_string(), "1".to_string());
}

#[test]
fn test_add_binary() {
    assert_eq!(Solution::add_binary("0".to_string(), "0".to_string()), "0".to_string());
}