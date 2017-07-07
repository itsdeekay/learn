import java.util.*;
import java.io.*;
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int R = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    String s;
    String result[] = new String[R];
    int n,flag;
    for (int i = 0; i < R; i++) {
      n = in.nextInt();
      s = in.nextLine();
      s = in.nextLine();
      flag =0;
      if(n%2==0){
          result[i] = "no";
          continue;
      }else{
          
          String str[] = s.split(" "); 
          int ns[] = new int[n];
          for(int j=0;j<n;j++){
              ns[j] = Integer.parseInt(str[j]);
          }
            
          int n2 = n/2;
          
          if(ns[n2]!=n2+1 || ns[0]!=1 || ns[n-1]!=1){
              result[i] = "no";
              continue;
              
          }else{
              for(int j=1;j<n2;j++){
                  if(ns[j]!=ns[n-1-j] || ns[j]!=ns[j-1]+1){
                     flag = 1;
                     break;
                  }
              }
          }
          if(flag==0)
              result[i] = "yes";
          else 
              result[i] = "no";
      }
      
    }
    for (int i = 0; i < R; i++) {
        System.out.println(result[i]);
    }
  }
}