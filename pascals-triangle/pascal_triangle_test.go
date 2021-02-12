package pascal

import (
	"reflect"
	"testing"
)

func TestGenerate(t *testing.T) {
	var testCases = []struct {
		numRows int
		want    [][]int
	}{
		{
			numRows: 1,
			want:    [][]int{[]int{1}},
		},
		{
			numRows: 0,
			want:    [][]int{},
		},
		{
			numRows: 5,
			want: [][]int{
				[]int{1},
				[]int{1, 1},
				[]int{1, 2, 1},
				[]int{1, 3, 3, 1},
				[]int{1, 4, 6, 4, 1},
			},
		},
	}

	for _, testCase := range testCases {
		if r := generate(testCase.numRows); !reflect.DeepEqual(r, testCase.want) {
			t.Errorf("generate(%d) == %v, expected %v", testCase.numRows, r, testCase.want)
		}
	}
}
