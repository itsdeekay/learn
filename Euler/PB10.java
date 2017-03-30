/*The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.*/

import java.util.Scanner;
import java.lang.*;

public class PB10{
	public static void main(String[] args) {
		long primes = 2;	
        boolean[] pass = new boolean[2000000];						// Creating array of upper size to keep record of primes
        
		for ( int i = 3; i < 2000000; i+=2 ) {
            if ( pass[i] == true ) continue;

            primes+=i;

            for ( int j = i+i; j < 2000000; j += i )
                pass[j] = true;
        }
		System.out.println("Sum of prime numbers upto 2 million is "+primes);
	}
}