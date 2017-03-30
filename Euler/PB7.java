/*By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?*/

import java.util.Scanner;
import java.lang.*;

public class PB7{
	public static void main(String[] args) {
		
        long primes = 1;
        int n = 10001;
        int max = (int)(n*Math.log(n)+n*Math.log(Math.log(n)));  	// nth prime lies in nlogn+n(loglogn-1) and nlogn+nloglogn
        boolean[] pass = new boolean[max];						// Creating array of upper size to keep record of primes
        
		for ( int i = 3; i < max; i+=2 ) {
            if ( pass[i] == true ) continue;

            primes++;

            if ( primes == 10001 ) {
                n = i;
                break;
            }

            for ( int j = i+i; j < max; j += i )
                pass[j] = true;
        }
        System.out.println("10001st prime is: "+ n);
    }
}
		