package main

func merge(nums1 []int, m int, nums2 []int, n int)  {
    cur := m+n-1
    cur1 := m-1
    cur2 := n-1
    
    for cur1 >= 0 && cur2 >= 0 {
        if nums1[cur1] >= nums2[cur2] {
            nums1[cur] = nums1[cur1]
            cur1--
        } else {
            nums1[cur] = nums2[cur2]
            cur2--
        }
        cur--
    }
    
    for cur2 >= 0 {
       nums1[cur] = nums2[cur2]
        cur2--
        cur--
    }
    
}
