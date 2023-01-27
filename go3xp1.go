package main

import ("fmt")

var x int

func main(){
	fmt.Print("Count: ")
	fmt.Scan(&x)
	if x <=0{
		fmt.Println("Number must be above 0")
		return
	}

	for x != 1{
		if (x%2) == 0 {
			x = x/2
		} else {
			x = 3*x+1
		}
		fmt.Println(x)
	}
}
