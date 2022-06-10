package main

import "fmt"

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	mod := numRows + (numRows - 2)
	result := make([]string, numRows)

	for i, r := range s {
		m := i % mod
		if m < numRows {
			result[m] = fmt.Sprintf("%s%s", result[m], string(r))
		} else {
			result[(numRows-1)-(m-(numRows-1))] = fmt.Sprintf("%s%s", result[(numRows-1)-(m-(numRows-1))], string(r))
		}
	}

	res := ""
	for _, row := range result {
		res = fmt.Sprintf("%s%s", res, row)
	}

	return res
}
