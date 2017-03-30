/*The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.*/

import java.util.Scanner;
import java.lang.*;

public class PB6{
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		System.out.print("Enter the Upper limit: ");
		int n = s.nextInt();
		
		int s1 = n*(n+1)*(2*n+1)/6;
		int s2 = (int)Math.pow(n*(n+1)/2,2);
		int diff = s2-s1;
		System.out.print("The Difference is : "+ diff);
	}
}
		