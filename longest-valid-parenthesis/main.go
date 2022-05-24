package main

type save struct {
    c byte
    i int
}

func longestValidParentheses(s string) int {
    n := len(s)
    stack := []save{}
    flag := make([]int, n)
    result := 0
    for i:=0; i<n; i++ {
        c := s[i]
        if c == '(' {
            stack = append(stack, save{c, i})
        } else {
            if len(stack) == 0 || stack[len(stack)-1].c != '(' {
                flag[i] = 0
            } else {
                v := stack[len(stack)-1]
                flag[i] = 1
                flag[v.i] = 1
                stack = stack[:len(stack)-1]
            }
        }
        
    }
    
    for len(stack) > 0 {
        v := stack[len(stack)-1]
        flag[v.i] = 0
        stack = stack[:len(stack)-1]
    }
    
    t := 0
    for _, v := range flag {
        if v == 1 {
            t++
        } else {
            t = 0
        }
        
        if t > result {
            result = t
        }
    }
    
    return result
}
