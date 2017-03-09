/*A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.*/

import java.util.Scanner;
import java.lang.*;

public class PB4{
	public static void main(String[] args) {
		
		int x,y,z,num,d,r;
		for(x=9;x>=1;x--){
			for(y=9;y>=0;y--){
				for(z=9;z>=0;z--){
					num = 9091*x + 910*y +100*z;				// num = 100000*x + 10000*y + 1000*z + 100*z + 10*y + x = 11*(9091x+910y+100z)
					for(d=90;d>=10;d--){						//num is divisible by 11 so at least one number is divisible by 11 which leaves 	number between 10-90
						if(num%d==0){
							if(num/d>999)
								break;
							else
								r = num*11;
								System.out.println("The largest prime is: "+r);
								return;
						}
					}
				}
			}
		}
	}
}