/*The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?*/


import java.util.Scanner;
import java.lang.*;

public class PB3{
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		long n = s.nextLong();
		long r = 1L;										//Pre setting the value of largest prime
		long i = 1L;
		if(n%2==0){
			r =2;
			while (n%2==0)
				n/=2;								//Checking no. for multiple of 2 and setting largest prime to 2
		}
		
		for (i=3;i<Math.sqrt(n);i+=2){
			if(n%i==0){
				r = i;								// checking no. for prime factors in steps of 2 and setting largest value to r
				while(n%i==0)
					n /= i;
			}
		}
		
		//Comparing values of r and n for largest prime
		if(r>n)
			System.out.println("The largest Prime Factor is "+ r);
		else
			System.out.println("The largest Prime Factor is "+ n);
	}
	
}