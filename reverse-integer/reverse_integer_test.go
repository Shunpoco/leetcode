package reverse

import "testing"

func TestReverse(t *testing.T) {
	testCases := []struct {
		x    int32
		want int32
	}{
		{x: 123, want: 321},
		{x: -123, want: -321},
		{x: 0, want: 0},
		{x: 123000, want: 321},
		{x: 2147483647, want: 0},
	}

	for idx, testCase := range testCases {
		if reverseInteger(testCase.x) != testCase.want {
			t.Errorf("%d is failed.", idx)
		}
	}
}
