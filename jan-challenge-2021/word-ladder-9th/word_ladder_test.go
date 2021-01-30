package wordLadder

import "testing"

func TestWordLadder(t *testing.T) {
	testCases := []struct {
		beginWord string
		endWord   string
		wordList  []string
		Output    int
	}{
		{
			beginWord: "hit",
			endWord:   "cog",
			wordList:  []string{"hot", "dot", "dog", "lot", "log", "cog"},
			Output:    5,
		},
		{
			beginWord: "hit",
			endWord:   "cog",
			wordList:  []string{"hot", "dot", "dog", "lot", "log"},
			Output:    0,
		},
		{
			beginWord: "red",
			endWord:   "tax",
			wordList:  []string{"ted", "tex", "red", "tax", "tad", "den", "rex", "pee"},
			Output:    4,
		},
		{
			beginWord: "dog",
			endWord:   "hng",
			wordList:  []string{"dog", "hng"},
			Output:    0,
		},
	}

	for idx, testCase := range testCases {
		res := ladderLength(testCase.beginWord, testCase.endWord, testCase.wordList)
		if res != testCase.Output {
			t.Errorf("%d failed: %d is not %d", idx, testCase.Output, res)
		}
	}
}
