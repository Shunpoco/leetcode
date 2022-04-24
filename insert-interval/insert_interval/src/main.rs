struct Solution;
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        if intervals.len() == 0 {
            return vec![new_interval.clone()];
        }
        
        let (mut left, mut right) = (0 as i32, (intervals.len()-1) as i32); // i32でやっておかないと、right = -1, left = 0 という状況の時にRuntime errorが発生する
        let (mut stop_left, mut stop_right) = (false, false);
        while (!stop_left || !stop_right) && left <= right {
            if intervals[left as usize][1] < new_interval[0] {
                left += 1;
            } else {
                stop_left = true;
            }
            
            if intervals[right as usize][0] > new_interval[1] {
                right -= 1;
            } else {
                stop_right = true;
            }
        }
        
        let mut result = vec![];
        if left > right {
            for v in &intervals[0..(right+1) as usize] {
                result.push(v.clone());
            }
            result.push(new_interval.clone());
            for v in &intervals[left as usize..] {
                result.push(v.clone());
            }
        } else {
            for v in &intervals[0..left as usize] {
                result.push(v.clone());
            }
            let s = if intervals[left as usize][0] < new_interval[0] { intervals[left as usize][0] } else { new_interval[0] };
            let e = if intervals[right as usize][1] > new_interval[1] { intervals[right as usize][1] } else { new_interval[1] };
            result.push(vec![s, e]);
            for v in &intervals[(right+1) as usize..] {
                result.push(v.clone());
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::insert(vec![vec![1,3], vec![6,9]], vec![2,5]), vec![vec![1,5], vec![6,9]]);
}
