package pascal

import (
	"reflect"
	"testing"
)

func TestGetRow(t *testing.T) {
	var testCases = []struct {
		rowIndex int
		want     []int
	}{
		{3, []int{1, 3, 3, 1}},
		{0, []int{1}},
		{1, []int{1, 1}},
	}

	for _, testCase := range testCases {
		if r := getRow(testCase.rowIndex); !reflect.DeepEqual(r, testCase.want) {
			t.Errorf("getRow(%d) == %v, expected %v", testCase.rowIndex, r, testCase.want)
		}
	}
}
