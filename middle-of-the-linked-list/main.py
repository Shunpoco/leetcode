// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn middle_node(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l = 0usize;
        let mut cout = head.as_ref();
        
        while let Some(node) = cout {
            cout = node.next.as_ref();
            l += 1;
        }
        
        for _ in 0..l/2 {
            head = head.unwrap().next;
        }
        
        head
    }
}

