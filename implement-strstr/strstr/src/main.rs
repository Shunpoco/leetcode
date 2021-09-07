struct Solution {}

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let mut h_c: Vec<char> = haystack.chars().collect();
        let mut n_c: Vec<char> = needle.chars().collect();
        
        let l_h = h_c.len() as usize;
        let l_n = n_c.len() as usize;
        

        if l_n == 0 {
            return 0;
        }

        if l_h < l_n {
            return -1;
        }

        let mut i_h = 0usize;
        
        while i_h <= l_h - l_n {
            let mut temp_i_h = i_h;
            for i_n in 0..l_n {
                if h_c[temp_i_h] != n_c[i_n] {
                    break;
                }
                if i_n == l_n - 1 {
                    return i_h as i32;
                }
                temp_i_h += 1;
            }
            i_h += 1;
        }
        -1
    }
}

fn main() {
    println!("Hello, world!");
}
