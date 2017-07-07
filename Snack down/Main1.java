import java.util.*;
import java.io.*;
public class Main1 {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int R = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    String result[] = new String[R];
    int n,flag,x11,x12,y11,y12,x21,x22,y21,y22,f;
    for (int i = 0; i < R; i++) {
      flag =0;
      f=0;
      x11 = in.nextInt();
      y11 = in.nextInt();
      x12 = in.nextInt();
      y12 = in.nextInt();
      x21 = in.nextInt();
      y21 = in.nextInt();
      x22 = in.nextInt();
      y22 = in.nextInt();
      if(x11 == x21) flag +=1;
      if(x12 == x22) flag +=1;
      if(y11 == y21) flag +=1;
      if(y12 == y22) flag +=1;
      if(flag<2){
          result[i] = "no";
          continue;
      } else{
          if(Math.abs(x11)>Math.abs(x21)) f+=1;
          if(Math.abs(x12)>Math.abs(x22)) f+=1;
          if(Math.abs(y11)>Math.abs(y21)) f+=1;
          if(Math.abs(y12)>Math.abs(y22)) f+=1;
          if(f==0){
              if(Math.abs(x11)<Math.abs(x21)) f+=1;
              if(Math.abs(x12)<Math.abs(x22)) f+=1;
              if(Math.abs(y11)<Math.abs(y21)) f+=1;
              if(Math.abs(y12)<Math.abs(y22)) f+=1;
          }
          if(f==2){
              result[i] = "no";
              continue;
          } else{
              result[i] = "yes";
              continue;
          }
      }
    }
    for (int i = 0; i < R; i++) {
        System.out.println(result[i]);
  }
}
}