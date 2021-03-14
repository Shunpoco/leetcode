package reverse

func reverseString(s []byte) {
	reverse(&s)
}

func reverse(s *[]byte) {
	length := len(*s)
	mid := length / 2
	for i := 0; i < mid; i++ {
		t := (*s)[i]
		(*s)[i] = (*s)[length-1-i]
		(*s)[length-1-i] = t
	}
}
