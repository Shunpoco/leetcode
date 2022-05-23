package main

import "fmt"

type count struct {
    zero int
    one int
}

func findMaxForm(strs []string, m int, n int) int {
    counter := make(map[count]int)
    keys := []count{}
    for _, str := range strs {
        zero := 0
        one := 0
        for _, c := range str {
            if c == '0' {
                zero++
            } else {
                one++
            }
        }
        c := count{zero, one}
        if _, p := counter[c]; !p {
            keys = append(keys, c)
        }
        counter[c]++
    }
    
    // fmt.Println(counter)
    
    result := dp(0, 0, 0, m, n, &counter, &keys)
    
    return result
}

func dp(cm, cn, idx, m, n int, counter *map[count]int, keys *[]count) int {
    if m < cm || n < cn {
        return -1
    }
    
    if idx == len(*keys) {
        return 0
    }
    
    var result int
    key := (*keys)[idx]
    for i:=0; i<(*counter)[key]+1; i++ {
        t := dp(cm+key.zero*i, cn+key.one*i, idx+1, m, n, counter, keys)
        if t >= 0 {
            t += i
            if t > result {
                result = t
            }
        }
    }
    
    return result
}
