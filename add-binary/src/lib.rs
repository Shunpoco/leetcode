struct Solution;
impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut a = a.chars().rev().peekable();
        let mut b = b.chars().rev().peekable();

        let mut carry = 0;
        let mut result = vec![];

        while a.peek().is_some() && b.peek().is_some() {
            let va=  a.next().unwrap();
            let vb = b.next().unwrap();

            let mut bits = carry;
            if va == '1' {
                bits += 1;
            }
            if vb == '1' {
                bits += 1;
            }
            
            if bits >= 2 {
                carry = 1;
            } else {
                carry = 0;
            }

            if bits % 2 == 1 {
                result.push('1');
            } else {
                result.push('0');
            }
        }

        while a.peek().is_some() {
            let va = a.next().unwrap();
            let mut bits = carry;
            if va == '1' {
                bits += 1;
            }
            if bits == 2 {
                carry = 1;
            } else {
                carry = 0;
            }
            if bits % 2 == 1 {
                result.push('1');
            } else {
                result.push('0');
            }
        }

        while b.peek().is_some() {
            let vb = b.next().unwrap();
            let mut bits = carry;
            if vb == '1' {
                bits += 1;
            }
            if bits == 2 {
                carry = 1;
            } else {
                carry = 0;
            }
            if bits % 2 == 1 {
                result.push('1');
            } else {
                result.push('0');
            }
        }

        if carry == 1 {
            result.push('1');
        }

        result.iter().rev().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn fist() {
        let a = "11".to_string();
        let b = "1".to_string();

        assert_eq!("100".to_string(), Solution::add_binary(a, b));
    }

    #[test]
    fn second() {
        let a = "1010".to_string();
        let b = "1011".to_string();

        assert_eq!("10101".to_string(), Solution::add_binary(a, b));
    }
}
