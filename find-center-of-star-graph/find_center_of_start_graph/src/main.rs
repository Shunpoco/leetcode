struct Solution {}

impl Solution {
    pub fn find_center(edges: Vec<Vec<i32>>) -> i32 {
        let mut center1 = 0i32;
        let mut center2 = 0i32;

        for edge in edges {
            let v1 = edge[0];
            let v2 = edge[1];

            if v1 == center1 || v1 == center2 {
                return v1;
            } else if v2 == center1 || v2 == center2 {
                return v2;
            }
            
            center1 = v1;
            center2 = v2;
            
        }
        
        0
    }
}

fn main() {
    assert_eq!(Solution::find_center(vec![vec![1,3], vec![2,3]]), 3);
}
