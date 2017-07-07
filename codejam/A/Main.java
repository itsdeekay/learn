import java.util.*;
import java.io.*;
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    String s[] = new String[t];
    int k[] = new int[t];
    int r[] = new int[t];
    for (int i = 0; i < t; ++i) {
      s[i] = in.next();
      k[i] = in.nextInt();
      int ln = s[i].length();
      r[i] = 0;
      String str[] = s[i].split("");
      
      for(int j=0;j<=ln-k[i];j++){
          if(str[j].equals("-")){
              //System.out.println("at j:"+j);
              r[i]++;

              for(int l=0;l<k[i];l++){
                if(str[j+l].equals("-"))
                    str[j+l] = "+";
                else
                    str[j+l] = "-";
              }
          }
      }
      for (int j=0;j<ln;j++){
          if(str[j].equals("-")){
              r[i] = -1;
              break;
          }
      }  
    }
    for(int i=0;i<t;i++){
        if(r[i]==-1)
            System.out.println("Case #" + (i+1) + ": " +"IMPOSSIBLE");
        else
            System.out.println("Case #" + (i+1) + ": " +r[i]);
    }
  }
}
