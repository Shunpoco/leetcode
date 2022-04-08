struct Solution;
impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        let mut stack = vec![vec![]];
        let mut result = vec![];
        
        while stack.len() > 0 {
            let v = stack.pop().unwrap();
            
            if v.len() == turned_on as usize {
                let s = convert(&v);
                if s.len() > 0 {
                    result.push(s.clone());
                }
            }
            
            let start = if v.len() == 0 { 0 } else { v[v.len()-1]+1 };
            
            for i in start..10 {
                let mut t = v.clone();
                t.push(i);
                stack.push(t);
            }
        }
        
        result
    }
}

fn convert(bits: &Vec<usize>) -> String {
    let mut hours = 0i32;
    let mut minutes = 0i32;
    
    for &bit in bits {
        match bit {
            0 => { hours += 8; },
            1 => { hours += 4; },
            2 => { hours += 2; },
            3 => { hours += 1; },
            4 => { minutes += 32; },
            5 => { minutes += 16; },
            6 => { minutes += 8; },
            7 => { minutes += 4; },
            8 => { minutes += 2; },
            _ => { minutes += 1; },
        }
    }
    
    if hours > 11 || minutes > 59 {
        return "".to_string();
    }
    
    
    format!("{}:{}{}", hours, if minutes < 10 { "0" } else { "" }, minutes)
}


fn main() {
    assert_eq!(Solution::read_binary_watch(9), Vec::<String>::new());
}
