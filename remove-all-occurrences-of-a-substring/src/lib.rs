struct Solution;
impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        let l = part.len();

        let mut v = Vec::new();

        for c in s.chars() {
            v.push(c);
            if v.len() >= l && same(&v[v.len()-l..], &part) {
                v = v[..v.len()-l].to_vec();
            }
        }

        v.into_iter().collect()
    }
}

fn same(v: &[char], part: &str) -> bool {
    let s: String = v.iter().collect();

    s == part
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let s = String::from("daabcbaabcbc");
        let part = String::from("abc");

        let got = Solution::remove_occurrences(s, part);

        assert_eq!(String::from("dab"), got);
    }

    #[test]
    fn second() {
        let s = String::from("axxxxyyyyb");
        let part = String::from("xy");

        let got = Solution::remove_occurrences(s, part);

        assert_eq!(String::from("ab"), got);
    }
}
