struct MyQueue {
    s1: Vec<i32>,
    s2: Vec<i32>,
    front: i32,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        MyQueue{
            s1: vec![],
            s2: vec![],
            front: 0,
        }
    }
    
    fn push(&mut self, x: i32) {
        self.s1.push(x);
        if self.s1.len() == 1 {
            self.front = x;
        }
    }
    
    fn pop(&mut self) -> i32 {
        while self.s1.len() > 0 {
            let v = self.s1.pop().unwrap();
            if self.s1.len() == 1 {
                self.front = v;
            }
            self.s2.push(v);
        }
        
        let v = self.s2.pop().unwrap();
        
        while self.s2.len() > 0 {
            self.s1.push(self.s2.pop().unwrap());
        }
        
        v
    }
    
    fn peek(&self) -> i32 {
        self.front
    }
    
    fn empty(&self) -> bool {
        self.s1.len() == 0
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */

fn main() {
    let mut obj = MyQueue::new();
    obj.push(32);
    println!("{}", obj.pop());
}
