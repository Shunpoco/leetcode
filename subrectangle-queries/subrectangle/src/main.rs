struct SubrectangleQueries {
    rows :usize,
    cols :usize,
    rectangle :Vec<Vec<i32>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SubrectangleQueries {

    fn new(rectangle: Vec<Vec<i32>>) -> Self {
        SubrectangleQueries{
            rows: rectangle.len(),
            cols: rectangle[0].len(),
            rectangle: rectangle,
        }  
    }
    
    fn update_subrectangle(&mut self, row1: i32, col1: i32, row2: i32, col2: i32, new_value: i32) {
        if row2 >= self.rows as i32 || col2 >= self.cols as i32 {
            return
        }
        
        for row in row1..row2+1 {
            for col in col1..col2+1 {
                self.rectangle[row as usize][col as usize] = new_value;
            }
        }
    }
    
    fn get_value(&self, row: i32, col: i32) -> i32 {
        self.rectangle[row as usize][col as usize]
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * let obj = SubrectangleQueries::new(rectangle);
 * obj.update_subrectangle(row1, col1, row2, col2, newValue);
 * let ret_2: i32 = obj.get_value(row, col);
 */

fn main() {
    let mut sr = SubrectangleQueries::new(vec![vec![1,2,3], vec![2,3,4]]);
    println!("{}", sr.get_value(0, 0));
    sr.update_subrectangle(0, 0, 1, 2, 4);
    println!("{}", sr.get_value(0, 0));
}
