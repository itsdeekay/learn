import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) {
    Scanner iin = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = iin.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    int N[] = new int[t];
    int K[] = new int[t];
    int len, pos;
    int Max[] = new int[t];
    int Min[] = new int[t];
    
    for (int i = 0; i < t; ++i) {
      N[i] = iin.nextInt();
      K[i] = iin.nextInt();
      if(K[i]>=N[i]/2){
         Max[i] = 0; Min[i] =0;
         continue;         
      }
      int st[] = new int[N[i]+2];
      st[0] = 1; st[N[i]+1] = 1;
      Max[i] = 0; Min[i] =0;
      
        for(int j=1;j<=K[i];j++){
            int large =0;
            len=0;pos = 0;
            for (int k=1;k<=N[i];k++){
                if(st[k]==0){
                    
                  len++;
                  if (len>=large){
                     large = len;
                     pos = k;
                  } 
                } else{
                  len =0;
                }
            }
            int initial = pos-large;
            if(large%2==0){
              st[initial+large/2] = 1;
            } else{
                st[initial+1+large/2] = 1;
            }
            if(j == K[i]){
                if(large%2==0){
                  Max[i] = large/2;
                  Min[i] = Max[i]-1;
                } else{
                    Max[i] = Min[i] = large/2;
                }
            }
      }  
    }
    for(int i=0;i<t;i++){
            System.out.println("Case #" + (i+1) + ": " +Max[i]+" "+Min[i]);
    }
  }
}
