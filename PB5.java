/*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?*/

import java.util.Scanner;
import java.lang.*;

public class PB5{
	public static void main(String[] args) {
		
		long l=1;
		for(long i=2;i<=20;i++)
		{
		 l*= i/gcd(l,i);						// Iterating through 2-20 for calculating least commmon factor for 1-20
		}   
		System.out.println("The smallest positive number divisible by 1-20 is "+l);
	}
	
	//returns greatest common divisor
	static long gcd(long a, long b) {
		while(b > 0) {
			a %= b;
			if (a == 0) return b;
			b %= a;
		}
		return a;
	}
}