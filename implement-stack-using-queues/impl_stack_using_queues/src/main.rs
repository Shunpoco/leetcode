use std::collections::VecDeque;

struct MyStack {
    q1: VecDeque<i32>,
    q2: VecDeque<i32>,
    top: i32,
    len: usize,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {

    fn new() -> Self {
        MyStack{
            q1: VecDeque::new(),
            q2: VecDeque::new(),
            top: 0,
            len: 0,
        }        
    }
    
    fn push(&mut self, x: i32) {
        self.q1.push_back(x);
        self.top = x;
        self.len += 1;
    }
    
    fn pop(&mut self) -> i32 {
        while self.q1.len() > 1 {
            let v = self.q1.pop_front().unwrap();
            self.q2.push_back(v);
        }
        let result = self.q1.pop_front().unwrap();
        self.top = 0;
        self.len -= 1;
        while self.q2.len() > 0 {
            let v = self.q2.pop_front().unwrap();
            self.q1.push_back(v);
            if self.q2.len() == 0 {
                self.top = v;
            }
        }
        
        result
    }
    
    fn top(&self) -> i32 {
        self.top
    }
    
    fn empty(&self) -> bool {
        self.len == 0
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */


fn main() {}
