import java.util.*;
import java.io.*;
public class Snake {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int R = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    String s;
    String result[] = new String[R];
    int n,flag;
    for (int i = 0; i < R; i++) {
      n = in.nextInt();
      flag = 0;
      s = in.next();
      String str[] = s.split("");
      int n1 = str.length;
      for(int j=0;j<n1;j++){
          if(flag==0){
              if(str[j].equals(".")){continue;}
                  
              else if(str[j].equals("H")){flag = 1;}
                  
              else if(str[j].equals("T")){flag =2;}
                  
          }else if(flag==1){
              if(str[j].equals(".")){continue;}
              else if(str[j].equals("H")){flag =2;}
              else if(str[j].equals("T")){flag = 0;}
          } if(flag ==2)
              break;
      }
      if(flag==0)
              result[i] = "Valid";
      else if(flag ==1 || flag ==2)
              result[i] = "Invalid";
    }
    for (int i = 0; i < R; i++) {
        System.out.println(result[i]);
    }
  }
}