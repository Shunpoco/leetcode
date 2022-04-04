struct Solution;
impl Solution {
    pub fn get_permutation(n: i32, mut k: i32) -> String {
        let mut visit = vec![true;n as usize];
        let mut digits = vec![];
        let mut v = 1i32;
        let mut result = "".to_string();
        for i in 1..n {
            v *= i;
            digits.push(v);
        }        
        // println!("{:?}", digits);
        
        while k > 0 && digits.len() > 0 {
            let v = digits.pop().unwrap();
            let c = (k as f64 / v as f64).ceil() as usize;
            // println!("{}", c);
            let mut count = 0usize;
            let mut idx = 0usize;
            while count < c {
                if visit[idx] {
                    count += 1;
                }
                if count == c {
                    // result.push((idx+1) as i32);
                    result = format!("{}{}", result, (idx+1));
                    visit[idx] = false;
                }
                idx += 1;
            }
            
            k -= v * (c as i32 - 1);
        }
        
        for (i, &v) in visit.iter().enumerate() {
            if v {
                result = format!("{}{}", result, (i+1));
                // result.push(i as i32+1);
                break;
            }
        }
        
        // println!("{:?}", result);
        // println!("{:?}", visit);
        result
        // result.into_iter().map(|x| x.to_string()).collect::<String>()
    }
}

fn main() {
    assert_eq!(Solution::get_permutation(3, 3), "213".to_string());
}
