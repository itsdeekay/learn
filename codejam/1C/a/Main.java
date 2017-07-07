import java.util.*;
import java.io.*;
import java.lang.Math.*;

public class Main {
  public static void main(String[] args) {
    Scanner iin = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = iin.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    int R[] = new int[t];
    int H[] = new int[t];
   
    int N,K;
    
    for (int i = 0; i < t; ++i) {
      N = iin.nextInt();
      K = iin.nextInt();
      String A[][] = new String[N][2];
      for(int j = 0;j<N;j++){
        R[i] = iin.nextInt();
        H[i] = iin.nextInt();  
        A[i][0] = i+"";
        A[i][1] = Double.toString(Math.PI * R[i]*R[i]+ Math.PI*2*R[i]*H[i]);
      }
      Arrays.sort(A, new Comparator<String[]>() {
            @Override
            public int compare(final String[] o1, final String[] o2) {
                double val1 = Double.valueOf(o1[1]);
                double val2 = Double.valueOf(o2[1]);
                // Ascending
                if (val1 < val2) {
                    return 1;
                } else if (val1 == val2) {
                    return 0;
                }
                return -1;
            }    
        });
      
     for(int k=0;k<N;k++){
            System.out.println(A[k]);
      
    }
    /*for(int i=0;i<t;i++){
            System.out.println("Case #" + (i+1) + ": " +Max[i]+" "+Min[i]);
    }*/
  }
}
}
