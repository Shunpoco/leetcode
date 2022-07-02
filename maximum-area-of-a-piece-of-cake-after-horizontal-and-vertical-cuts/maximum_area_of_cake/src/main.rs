struct Solution;
impl Solution {
    pub fn max_area(h: i32, w: i32, mut horizontal_cuts: Vec<i32>, mut vertical_cuts: Vec<i32>) -> i32 {
        let MOD = 1_000_000_007 as i64;
        
        horizontal_cuts.sort();
        vertical_cuts.sort();
        
        let mut cum_h = Vec::with_capacity(horizontal_cuts.len()+1);
        let mut cum_v = Vec::with_capacity(vertical_cuts.len()+1);
        
        for (i, &v) in horizontal_cuts.iter().enumerate() {
            if i == 0 {
                cum_h.push(v);
            } else {
                cum_h.push(v-horizontal_cuts[i-1]);
            }
        }
        cum_h.push(h-horizontal_cuts[horizontal_cuts.len()-1]);
        
        for (i, &v) in vertical_cuts.iter().enumerate() {
            if i == 0 {
                cum_v.push(v);
            } else {
                cum_v.push(v-vertical_cuts[i-1]);
            }
        }
        cum_v.push(w-vertical_cuts[vertical_cuts.len()-1]);
        
        let max_h = *cum_h.iter().max().unwrap() as i64;
        let max_v = *cum_v.iter().max().unwrap() as i64;
        
        // println!("{:?}", cum_h);
        // println!("{:?}", cum_v);
        
        (max_h*max_v%MOD) as i32
    }
}

fn main() {
    assert_eq!(Solution::max_area(1000000000, 1000000000, vec![2], vec![2]), 81);
}
