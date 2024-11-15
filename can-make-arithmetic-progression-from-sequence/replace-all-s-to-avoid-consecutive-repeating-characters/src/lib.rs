pub struct Solution;
impl Solution {
    pub fn modify_string(s: String) -> String {
        let cs: Vec<char> = s.chars().collect();

        let mut result = String::from("");

        for i in 0..cs.len() {
            let mut v = cs[i];
            if cs[i] == '?' {
                v = 'a';
                if i > 0 && cs[i-1] == v {
                    v = ((v as u8) + 1) as char;
                }

                if i < cs.len()-1 && cs[i+1] == v {
                    v = ((v as u8) + 1) as char;
                }
            }

            result.insert(result.len(), v);
        }

        result
    }
}

#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn case1() {
        let s = String::from("?zs");

        let got = Solution::modify_string(s);

        assert_eq!(got, String::from("azs"));
    }

    #[test]
    fn case2() {
        let s = String::from("ubv?w");

        let got = Solution::modify_string(s);

        assert_eq!(got, String::from("ubvaw"));
    }
}
