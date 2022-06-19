package main

import "sort"

func suggestedProducts(products []string, searchWord string) [][]string {
    sort.Slice(products, func(i, j int) bool { return products[i] < products[j] })
    memory := invertedIndex(&products)
    
    result := [][]string{}
    for i := 1; i <= len(searchWord); i++ {
        prefix := searchWord[:i]
        candidates := memory[prefix]
        t := []string{}
        for j := 0; j < len(candidates) && j < 3; j++ {
            t = append(t, products[candidates[j]])
        }        
        result = append(result, t)
    }
    
    return result
}

func invertedIndex(words *[]string) map[string][]int {
    result := make(map[string][]int)
    
    for idx, word := range *words {
        for i := 1; i <= len(word); i++ {
            if _, ok := result[word[:i]]; ok {
                result[word[:i]] = append(result[word[:i]], idx)
            } else {
                result[word[:i]] = []int{idx}
            }
        }
    }
    
    return result
}
