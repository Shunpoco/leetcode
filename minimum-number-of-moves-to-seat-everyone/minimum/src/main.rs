struct Solution {}

impl Solution {
    pub fn min_moves_to_seat(seats: Vec<i32>, students: Vec<i32>) -> i32 {
        let mut seats = seats;
        let mut students = students;
        
        seats.sort();
        students.sort();
        
        let mut result = 0i32;
        
        for i in 0..seats.len() {
            let v1 = seats[i];
            let v2 = students[i];
            let mut v = v1 - v2;
            if v < 0 {
                v = -1 * v;
            }
            
            result += v;
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::min_moves_to_seat(vec![3,1,5], vec![2,7,4]), 4);
} 
