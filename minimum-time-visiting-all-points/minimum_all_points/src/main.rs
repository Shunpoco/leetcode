struct Solution {}

impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut result = 0i32;

        for i in 0..points.len()-1 {
            let v1 = &points[i];
            let v2 = &points[i+1];
            result += Solution::bigger(
                Solution::abs(v2[0]-v1[0]),
                Solution::abs(v2[1]-v1[1]),
            );
        }
        
        result
    }
    
    fn abs(a: i32) -> i32 {
        if a < 0 {
            return -a;
        }
        a
    }
    
    fn bigger(a: i32, b: i32) -> i32 {
        if a > b {
            return a;
        }
        
        b
    }
}


fn main() {
    assert_eq!(Solution::min_time_to_visit_all_points(vec![vec![1, 1], vec![3, 4], vec![-1, 0]]), 7);
}
