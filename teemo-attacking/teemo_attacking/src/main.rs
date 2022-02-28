struct Solution;
impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        let mut result = vec![];
        
        for (idx, time) in time_series.iter().enumerate() {
            let v: i32;
            if idx == time_series.len()-1 {
                v = duration;
            } else {
                if time_series[idx+1] - time < duration {
                    v = time_series[idx+1]-time;
                } else {
                    v = duration;
                }
            }
            result.push(v);
        }
        
        println!("{:?}", result);
        
        return result.iter().sum::<i32>();
    }
}

fn main() {
    assert_eq!(Solution::find_poisoned_duration(vec![1, 2], 2), 3);
}
