/*

Project Euler problem number 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

*/

import java.util.Scanner;

public class PB1{
	public static void main(String args[]){
		int sum;
		Scanner s = new Scanner(System.in);
		System.out.print("Enter the Upper Limit: ");
		int n = s.nextInt();													   	//Taking input the upper limit for caclulating sum
		
		sum = 3*SOS((int)(n-1)/3) + 5*SOS((int)(n-1)/5) - 15*SOS((int)(n-1)/15); 	//calling SOS() with args by dividing the upper limit by divider to reduce the domain of problem
		System.out.println("The sum is: " + sum);
	}
	
	static int SOS(int n ){    														//Sum of series
		return n*(n+1)/2;
	}
}