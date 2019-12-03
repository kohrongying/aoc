package main

import (
	"fmt"
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestSeenTwice(t *testing.T) {
	ans := seenTwice("bababc")
	assert.True(t, ans)
}

func TestSeenThrice(t *testing.T) {
	ans := seenThrice("bababc")
	assert.True(t, ans)
}

func TestGetCounts(t *testing.T) {
	ans := getCounts("bababc")
	// fmt.Printf("%#v", ans)
	assert.Equal(t, map[int32]int{'b':3, 'a':2, 'c':1}, ans)
}

func TestHammingDistance(t *testing.T) {
	type testCase struct {
		expected int 
		s1, s2 string	
	}
	testCases := []testCase{
		{1, "abcde", "abede"},
		{2, "abcde", "aacdd"},
	}
	for _, c := range testCases {
		t.Run(fmt.Sprintf("%s %s", c.s1, c.s2), 
		func(t *testing.T){
			assert.Equal(t, c.expected, hammingDistance(c.s1, c.s2))
		})
	}
}

func TestGetPair(t *testing.T) {
	type testCase struct {
		expected [2]string
		input []string
	}
	testCases := []testCase{
		{[2]string{"fghij", "fguij"}, 
		[]string{"abcde", "fghij","klmno","pqrst","fguij","wvxyz"}},
		{[2]string{"mxhwoglxgeauywfdkztndcvjqr", "mxhwoglxgeauywfikztndcvjqr"}, SplitString(input)},
	}

	for _, c := range testCases {
		t.Run("", 
		func(t *testing.T){
			expected := getPair(c.input)
			assert.Equal(t, c.expected, expected)
		})
		
	}
}

func TestLastTest(t *testing.T) {
	assert.Equal(t, "mxhwoglxgeauywfkztndcvjqr", getCommonLetters("mxhwoglxgeauywfdkztndcvjqr", "mxhwoglxgeauywfikztndcvjqr"))
}

const input = `myhposlqgeauywfikztndcvrqr
	mbhposlxfeauywoikztndcvjqi
	mbhpoulxgeagywfikytndcvjqr
	jbhposlxgeauywdikztndcvjqk
	mbhpsslxueauywfikzfndcvjqr
	mbhposnxgeauzyfikztndcvjqr
	ibhposlxgetvywfikztndcvjqr
	mbcposlxgeauywfikztxdcvjqv
	mlhposltgeauywfikitndcvjqr
	mbhpostxgeauywfikztndjvjqy
	mboboslxglauywfikztndcvjqr
	mbhpoglxgeahywfikztndcvjqp
	mbhposlxgeapydpikztndcvjqr
	mbhposlxseauywfikztnncljqr
	mbhposlxgeauydfisztndcvjqj
	mbhposlxgeaugwwikzlndcvjqr
	mbhpoklxgeauywfikztndvvmqr
	mbhposlxgeauywfikdtndcmjqx
	mbhposlxaeauapfikztndcvjqr
	mbwposgxgeauymfikztndcvjqr
	mbhposlxgeauvwfirzcndcvjqr
	mbhpozlxgeaqywfykztndcvjqr
	mahqoslxgeauywfikzgndcvjqr
	mbhposlcgexbywfikztndcvjqr
	ykhposlxgeeuywfikztndcvjqr
	mbhgoswxgeauywfikztndhvjqr
	mbhposlxgeauywfikztnocmjqp
	mbvposfageauywfikztndcvjqr
	mbhpnslxgeauywfikztndgejqr
	mblposfxgeauypfikztndcvjqr
	mbhposlxyeauywfikzpndcvmqr
	ibhposlbgeauywfikotndcvjqr
	mbmposlxgeauywfiktwndcvjqr
	mbhposlxgeduywfikztndfvoqr
	mbhpoklxdeauywfikztndcvuqr
	mbhposlxgeauywfikltnlcvuqr
	mbhposlbgsauywfikztndsvjqr
	mbhposlxgeauywfirzfndcbjqr
	mphposlxgeauywfikztndcvjgg
	mohposlcgeauywfikzsndcvjqr
	mbhpovlxgeauyqfikotndcvjqr
	qbhpgslxgeauywqikztndcvjqr
	mbhposlxweauywfikztndtvjqm
	pbhposlxgeauywfikztnncvjqm
	mbbposlxpeauuwfikztndcvjqr
	mbhposlxgmauyrfikztndcvjir
	pbhposlqgefuywfikztndcvjqr
	mbhkoslxgeauywfikztndciwqr
	mbtpoflxgeauywfikztndrvjqr
	mbhcoslxveguywfikztndcvjqr
	mbhpovlxgeauywfhkdtndcvjqr
	mbhposlxgeauywftrztndcujqr
	mbhposlxgeaoywfdkzpndcvjqr
	mbnposlxgeyuywfikztldcvjqr
	mbaposlxweauywfikftndcvjqr
	mbhposljgeauywfikztcdcvvqr
	nbhpkslxgeauywfikzwndcvjqr
	mbhtoslxgeauywfikzkndcvjdr
	mbhposxxgeaxywfikztndsvjqr
	mbdpoflxgeauywfisztndcvjqr
	mbhposvxgeauywfikztnscvnqr
	mbcposlxghauywfikztndcgjqr
	mbhpovlxgeauywpckztndcvjqr
	mbhpfslxgeauywbikntndcvjqr
	mbhpowyxgeauywfikztndcvjcr
	mbhposlxoeatywfikztndcvoqr
	mchpfslxgeauywfikztidcvjqr
	mbhposvxgearywfikztndcvjcr
	mbhposlxgeauywfpcztnduvjqr
	mbhposlxgmauyyfiqztndcvjqr
	mbhposlxteauuwfikwtndcvjqr
	mbhpotlspeauywfikztndcvjqr
	mbhpoelxgeauywfikztndckjkr
	mbhpnslxgeauywfikztndcvkqs
	mbhpksfxgwauywfikztndcvjqr
	mxhwoglxgeauywfdkztndcvjqr
	mbhphsbjgeauywfikztndcvjqr
	mbhposlxgeauwifixztndcvjqr
	mbhposqxguauywfikztndcwjqr
	mbhposlngeauywfikztedcvjor
	nbhposlxgeauywiikztndcyjqr
	mbhposlxgeauawfykztndcvbqr
	mbhplslxgeauywcikztndcvjrr
	fshposlxgeagywfikztndcvjqr
	mbhposlxgeauymcikztndcxjqr
	mbhponlxgeauyloikztndcvjqr
	mbhposrxzeanywfikztndcvjqr
	mbhtoslxgeajyifikztndcvjqr
	mbhposixkeauywfikhtndcvjqr
	mahhoslxgeaufwfikztndcvjqr
	mbhpdslxteauywfikzvndcvjqr
	mfhposlxgeauywfiqttndcvjqr
	mbhplslxheauywfikztnscvjqr
	mbhpoylxgeauywbizztndcvjqr
	mbhposlhgeawywfjkztndcvjqr
	mbhkoslxgkauywfilztndcvjqr
	mbhposnxgeauywfikztkdcvlqr
	mvhpxslxgevuywfikztndcvjqr
	mbhpohlxgeauyrficztndcvjqr
	mbhsosuxgewuywfikztndcvjqr
	mbhpoxlxgeauywuikztnhcvjqr
	mbhposlxqeauyqfikztndcvrqr
	mbhpchlxgeauywfikztnhcvjqr
	mbhposlxgeauywoikztndcfqqr
	pbhposlxgeagmwfikztndcvjqr
	mxhwoglxgeauywfikztndcvjqr
	mbhpospxgaauywfikstndcvjqr
	mbhwoxlxgeauywfgkztndcvjqr
	mbhposlxgeauywfikvtndhvsqr
	mbbposlxgesuywfikztnicvjqr
	mhhjoslxgeauywfikztndccjqr
	mbhkoslxgeagywffkztndcvjqr
	mbhposlxgesqywfukztndcvjqr
	mbdposlxgeauywfilztndcvjqp
	mbhposlxgeakqwfikztedcvjqr
	mbhposuxgeayywficztndcvjqr
	mbhposlxgeauywfxkztndcloqr
	mchposlxgeauywoiiztndcvjqr
	tbhporlxgeauywfikztndcvyqr
	mbhposlxoevuywfikzindcvjqr
	qbhposlxfevuywfikztndcvjqr
	mbhposlxfeauvwfikztndcvgqr
	mbjposlxgsauywfikztnwcvjqr
	vbhposlxgeauvwfikztndcvjqk
	pbhposlxguauyrfikztndcvjqr
	mbhposlcgeauywfiketndcviqr
	mbsposlxgvauywfikztndcviqr
	mbhposlxgeauynfxkztndcvjbr
	mbhposlxtentywfikztndcvjqr
	mbhposlxgeavywfikztndhvjnr
	mbhpsvlxgeauywfikztndcvzqr
	mzhpotlxgeauywfiyztndcvjqr
	mbhposkqgeauywfiwztndcvjqr
	mbhposlxoeakywfikztndcvjqt
	mbhposlxghauywfikbdndcvjqr
	mbhpossxgeauywfikqxndcvjqr
	mbhposlxgearywhikztydcvjqr
	mbhposlxgeaiywfikztndfvjur
	mbhpxslxgoazywfikztndcvjqr
	mbhposlxneauywfibqtndcvjqr
	mnheoslxteauywfikztndcvjqr
	mbhposlxgeauywfmkztrdcvuqr
	mbhzowlxgeauywfizztndcvjqr
	mbhloslxgeauyofikztnucvjqr
	mbhposlxneagywfbkztndcvjqr
	mbhposongeauywfikztnzcvjqr
	mwyposlxgeauywfikztnqcvjqr
	mbhpnqaxgeauywfikztndcvjqr
	mboposlxzeauywfioztndcvjqr
	mbhposledeauywfikztndqvjqr
	mphpaslxgeauywfbkztndcvjqr
	mbhposrxgeauywlikbtndcvjqr
	ybhnoslxgeauywfihztndcvjqr
	mbhposlxgeauywfikntxccvjqr
	mbhposlxgeauqwfikutndcfjqr
	mbhposlxglabywfikztidcvjqr
	mbhpollxgeauywfikxtnscvjqr
	mboposlggeaufwfikztndcvjqr
	mbhposlxgeauywpikedndcvjqr
	mbhpoklxgeauywpikztndcvjlr
	mbhposhxgeauywfifztndcvpqr
	mbhposlxgwagywfikztndcvjwr
	mbhpokldgeauywfikztngcvjqr
	nbhposlxgeauywfiketndcvjxr
	mbhhoslxgexuywfikrtndcvjqr
	mbhposlxgefujwfikztkdcvjqr
	mbhposlxggagywfikztndchjqr
	mbhposlxgeauyvfilztnicvjqr
	mbhposlkgeauywfikzxndcvoqr
	mbhposlxgeauvqfikztndcvuqr
	zbhposlxgfauylfikztndcvjqr
	mbhyoshxgeauywfikztndcvjqa
	sbhposlxgeauyxfikztndavjqr
	mlhposlxgeauywfikzmndcqjqr
	mbhpaslxgekuywfikztnncvjqr
	ibhhoslxteauywfikztndcvjqr
	mbhposlxgeauyodibztndcvjqr
	mbhposlxgkaoywfikztndcvpqr
	mbhonslxgearywfikztndcvjqr
	mbdpoolxgealywfikztndcvjqr
	mbepfslxgvauywfikztndcvjqr
	mbhposlygeauywfikztfdcvaqr
	mthpoalxgeauywnikztndcvjqr
	mbhpesbogeauywfikztndcvjqr
	mbhposlxgjauywfikztnmcvjqj
	mbhnoslxgeauydfikgtndcvjqr
	mbhpxslxgeauywfikztndcvjcx
	muhposlxgwauywfipztndcvjqr
	mbhpcslxgeauywfiqztndcvjbr
	mbhpomlxgeauywfioftndcvjqr
	mbhposlfgepuywfikzmndcvjqr
	mbhsosliteauywfikztndcvjqr
	mbwposlxgeauywfikztnycveqr
	mbhpfslxgeauywfqkztndcvjhr
	mxhbvslxgeauywfikztndcvjqr
	fbhposlxgeauywfikzcnmcvjqr
	mbhfosfxgeauywfikztnduvjqr
	tbhporlxgeauywfikztndcvjqm
	mhhposlxgeauywfikctnecvjqr
	mbhposlxgeqtywfikztnmcvjqr
	qbhpjslxgeauywfikztndevjqr
	tbhpxslxgeaunwfikztndcvjqr
	wbhposlxgeadywfikztndcujqr
	mbhposlvgeauywfpkotndcvjqr
	mbhposlxgeagywfingtndcvjqr
	mbnposlxgeauywfikztnvcjjqr
	mohpoilxgeadywfikztndcvjqr
	mbhposlsgeauywfikztnxcvgqr
	mbhposlogeauywfikqtndcvjor
	mbhroslxgeauypfikztndcvjqg
	mblposuxgetuywfikztndcvjqr
	mbhposlogeiuywfikztodcvjqr
	mbhposlxgeauylfikztedcvrqr
	mbhfoslxgeautwxikztndcvjqr
	mbhouslxgeauywfikztnycvjqr
	mbhposlxgeauywfvkqtndlvjqr
	mbfposltgeauytfikztndcvjqr
	mbhposlxgcapywfikztnddvjqr
	hbhposlxgeasywfikztnxcvjqr
	mbhposntgeauywfikztcdcvjqr
	mbhponlxgfauywfirztndcvjqr
	mbhposlxgeatywlikztndcvrqr
	mohroslzgeauywfikztndcvjqr
	mbhpojaxgeauywfifztndcvjqr
	rbhposlxgwauywfikztndovjqr
	mbhpoclxgeaeywfikztndcvjqo
	mbhposllgeauywfikzondcvmqr
	mbhpxslxgeauywfikzymdcvjqr
	mbhposlxgeasywxikztndkvjqr
	mbhposlxgeauywfivztndcmjqx
	qbhposlxgpauywfikgtndcvjqr
	mbhposlxgeauyqdikztqdcvjqr
	cbhposlxgeauywfikttjdcvjqr
	mbhgoslxgeanywfihztndcvjqr
	mbhposlxgeajywfhkztndcvjvr
	mbhpozlxgeauewfmkztndcvjqr
	mbhposlxgeagywfbiztndcvjqr
	mbhmoslxgeauywfikztndrnjqr
	ybhposmxgeauywfikztndcviqr
	mrwposlxgeauywfikztndpvjqr
	mbhposlxneauywfikztndcbjqh
	mbhpowlxheauywfikztndcojqr
	mbeposlxgeauywfiwztnycvjqr
	mbhposixgeapywfikztndcvvqr
	mbhposlxgeauywfikztnbcvjap
	mzhposixgenuywfikztndcvjqr
	mbhposgxgeauywyikztndvvjqr
	mbhposajgeauywfikztzdcvjqr
	mbhyoslxgeauywfikzsndcvxqr
	mbhposlxgdauywfikmtndcljqr`