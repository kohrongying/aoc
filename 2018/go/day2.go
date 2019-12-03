package main
import "bytes"
func seenTwice(s string) bool {
	counts := make(map[rune]int)
	for _, e := range s {
		if _, ok := counts[e]; ok {
			counts[e] += 1
		} else {
			counts[e] = 1
		}
	}
	for _, value := range counts {
		if value == 2 {
			return true
		}
	} 
	return false
}

func seenThrice(s string) bool {
	counts := make(map[rune]int)
	for _, e := range s {
		if _, ok := counts[e]; ok {
			counts[e] += 1
		} else {
			counts[e] = 1
		}
	}
	for _, value := range counts {
		if value == 3 {
			return true
		}
	} 
	return false
}

func getCounts(s string) map[rune]int {
	counts := make(map[rune]int)
	for _, e := range s {
		if _, ok := counts[e]; ok {
			counts[e] += 1
		} else {
			counts[e] = 1
		}
	}
	return counts
}

func getChecksum(s string) int {
	twice_counts := 0
	thrice_counts := 0
	temp := SplitString(s)
	for _, x := range temp {
		if seenTwice(x) {
			twice_counts += 1
		}
		if seenThrice(x) {
			thrice_counts += 1
		}
	}
	return twice_counts * thrice_counts
}

func hammingDistance(s1, s2 string) int {
	count := 0
	for i, _ := range s1 {
		if s1[i] != s2[i] {
			count +=1 
		}
	}
	return count
}

func getPair(s []string) [2]string {
	for i := range s {
		for j := range s {
			if hammingDistance(s[i], s[j]) == 1 {
				return [2]string{s[i], s[j]}
			}
		}
	}
	panic("omgomgogm")
}

func getCommonLetters(s1, s2 string) string {
	var commons bytes.Buffer 
	for i, _ := range s1 {
		if s1[i] == s2[i] {
			commons.WriteByte(s1[i])
		}
	}
	return commons.String()
}