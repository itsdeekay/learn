/*A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.*/

import java.util.Scanner;
import java.lang.*;

public class PB9{
	public static void main(String[] args) {
		int a=0,b=0,c=0,flag=0;
		for(int i =2;i<500;i++){
			for(int j=1;j<i;j++){
				a = i*i-j*j;
				b = 2*i*j;
				c = i*i + j*j;

				if (a+b+c==1000){
					flag  = 1;
					break;
				}
			}
			if(flag==1)
				break;
		}
		
		System.out.println("The Product of triplet a+b+c =1000 is "+ a*b*c);
	}
}