package main

import (
	"testing"
)

// Test case must start with Cap T
func TestCompute(t *testing.T) {
	computed := compute(14)
	if computed != 2 {
		t.Errorf("Test failed, got: %d, want: %d", computed, 2)
	}
}

func TestFuelRecursion(t *testing.T) {
	total := fuelRecursion(14, 0)
	if total != 2 {
		t.Errorf("Test failed, got: %d, want: %d", total, 2)
	}

	total2 := fuelRecursion(1969, 0)
	if total2 != 966 {
		t.Errorf("Test failed, got: %d, want: %d", total2, 966)
	}

	total3 := fuelRecursion(100756, 0)
	if total3 != 50346 {
		t.Errorf("Test failed, got: %d, want: %d", total3, 50346)
	}
	
}