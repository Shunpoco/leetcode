struct Solution;
impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        let c: Vec<char> = expression.chars().collect();
        
        Self.exec(&c[..])
    }
    
    fn exec(self, c: &[char]) -> Vec<i32> {
        let mut res = vec![];
        
        for i in 0..c.len() {
            match c[i] {
                '+' | '-' | '*' => {
                    let a = &c[..i];
                    let b = &c[i+1..];
                    
                    let res_a = Self.exec(a);
                    let res_b = Self.exec(b);
                    
                    for &v in res_a.iter() {
                        for &k in res_b.iter() {
                            let val = match c[i] {
                                '+' => v+k,
                                '-' => v-k,
                                _ => v*k,
                            };
                            res.push(val);
                        }
                    }
                },
                _ => {},
            }
        }
        
        if res.len() == 0 {
            res.push(c.iter().collect::<String>().parse::<i32>().unwrap());
        }
        
        res
    }
}


fn main() {
    assert_eq!(Solution::diff_ways_to_compute("2-1-1".to_string()), vec![2, 0]);
}
