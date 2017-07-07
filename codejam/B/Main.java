import java.util.*;
import java.io.*;
public class Main {
  public static void main(String[] args) {
    Scanner iin = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = iin.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    long s[] = new long[t];
    int flag;
    long r[] = new long[t];
    
    for (int i = 0; i < t; ++i) {
      s[i] = iin.nextLong();
      r[i] = 0;
      
      for(long j=s[i];j>0;j--){
          flag =0;
          String st = String.valueOf(j);
          int ln = st.length();
          int in[] = new int[ln];
          String str[] = st.split("");
          for(int k=0;k<ln;k++){
            in[k] = Integer.parseInt(str[k]);
          }
          for(int k=0;k<ln-1;k++){
              if(in[k]>in[k+1]){
                  flag =1;
                  break;
              }
          }
          if(flag==0){
              r[i] = j;
              break;
          }
      }  
    }
    for(int i=0;i<t;i++){
            System.out.println("Case #" + (i+1) + ": " +r[i]);
    }
  }
}
