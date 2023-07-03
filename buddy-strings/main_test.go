package main

import "testing"

type test struct {
	name string
	s    string
	goal string
	want bool
}

func TestBuddyStrings(t *testing.T) {
	tests := []test{
		{
			name: "1",
			s:    "ab",
			goal: "ba",
			want: true,
		},
		{
			name: "2",
			s:    "ab",
			goal: "ab",
			want: false,
		},
		{
			name: "3",
			s:    "aa",
			goal: "aa",
			want: true,
		},
		{
			name: "4",
			s:    "abab",
			goal: "baba",
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := buddyStrings(tt.s, tt.goal); got != tt.want {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
