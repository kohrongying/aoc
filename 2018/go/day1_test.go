package main

import (
    "testing"
    "reflect"
)

func TestSplitString(t *testing.T) {
    total := SplitString(`+16
                    +1
                    +1`)
    ans := []string{"+16","+1","+1"}
    
    if !reflect.DeepEqual(total, ans) {
        t.Errorf("Sum was incorrect.")
    }
}

func TestSum(t *testing.T) {
    total := Sum(`+16
                +1
                -1`)
    if total != 16 {
        t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 16)
        }
}

func TestFindTwice(t *testing.T) {
    ans := findTwice(`+3
    +3
    +4
    -2
    -4`)
    if ans != 10 {
        t.Errorf("Incorrect")
    }
}