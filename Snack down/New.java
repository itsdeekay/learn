import java.util.*;
import java.io.*;
public class New {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int R = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    String result[] = new String[R];
    int x11,x12,y11,y12,x21,x22,y21,y22;
    for (int i = 0; i < R; i++) {
      result[i] = "no";
      x11 = in.nextInt();
      y11 = in.nextInt();
      x12 = in.nextInt();
      y12 = in.nextInt();
      x21 = in.nextInt();
      y21 = in.nextInt();
      x22 = in.nextInt();
      y22 = in.nextInt();
      
      if((x21==x11 && y21==y11)|| (x21==x12 && y21==y12) || (x22==x11 && y22==y11) || (x22==x12 && y22==y12)){
          result[i] = "yes";
          continue;
      }else if(x11==x12){
          if((y21>=y11 && y21<=y12)|| (y21<=y11 && y21>=y12) || (y22>=y11 && y22<=y12)|| (y22<=y11 && y22>=y12)){
              if(x21==x22 && x21==x12){
                  result[i] = "yes";
                  continue;
              }
          }
      }else if(y11==y12){
          if((x21>=x11 && x21<=x12)|| (x21<=x11 && x21>=x12) || (x22>=x11 && x22<=x12)|| (x22<=x11 && x22>=x12)){
              if(y21==y22 && y21==y11){
                  result[i] = "yes";
                  continue;
              }
          }
      }else{
          result[i] = "no";
          continue;
      }
    }
    for (int i = 0; i < R; i++) {
        System.out.println(result[i]);
  }
}
}