struct Solution;
impl Solution {
    pub fn construct_rectangle(area: i32) -> Vec<i32> {
        let mut memory = vec![false;area as usize + 1];
        memory[1] = true;
        memory[area as usize] = true;
        let mut L = area;
        let mut W = 1;
        
        let mut idx = 2;
        while idx*idx <= area {
            if !memory[idx as usize] {
                let mut t = idx;
                memory[t as usize] = true;
                while area % t == 0 {
                    let mut l = area / t;
                    let mut w = t;
                    if l < w {
                        let temp = l;
                        l = w;
                        w = temp;
                    }
                    if L - W > l - w {
                        L = l;
                        W = w;
                    }
                    t *= idx;
                    if t > area {
                        break;
                    }
                    memory[t as usize] = true;
                }
            }
            idx += 1;
        }
        
        Vec::from([L, W])
    }
}

fn main() {
    assert_eq!(Solution::construct_rectangle(4), vec![2, 2]);
}
