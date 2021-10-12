struct ParkingSystem {
    caps: Vec<Vec<i32>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {

    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem {
            caps: vec![
                Vec::with_capacity(big as usize),
                Vec::with_capacity(medium as usize),
                Vec::with_capacity(small as usize),
            ],
        }
    }
    
    fn add_car(&mut self, car_type: i32) -> bool {
        let num = (car_type - 1) as usize;
        if self.caps[num].capacity() == self.caps[num].len() {
            return false;
        } else {
            self.caps[num].push(1);
            true
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */

fn main() {
    let mut pk = ParkingSystem::new(1, 1, 1);
    println!("{}", pk.add_car(1));
    println!("{}", pk.add_car(2));
    println!("{}", pk.add_car(1));
}
