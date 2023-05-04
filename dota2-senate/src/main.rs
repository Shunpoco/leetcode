use std::collections::VecDeque;

struct Solution;
impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let senate = senate.chars();

        let mut rs = VecDeque::<usize>::new();
        let mut ds = VecDeque::<usize>::new();

        let mut n = 0;
        for (i, c) in senate.enumerate() {
            if c == 'R' {
                rs.push_back(i);
            } else {
                ds.push_back(i);
            }
            n += 1;
        }

        while rs.len() > 0 && ds.len() > 0 {
            let vr = rs.pop_front().unwrap();
            let vd = ds.pop_front().unwrap();

            if vr < vd {
                rs.push_back(vr+n);
            } else {
                ds.push_back(vd+n);
            }
        }

        if rs.len() > 0 {
            return String::from("Radiant");
        }

        String::from("Dire")
    }
}


fn main() {
    println!("{}", Solution::predict_party_victory(String::from("RDD")));
}
