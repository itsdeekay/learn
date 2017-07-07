import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) {
    Scanner iin = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = iin.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    int R[] = new int[t];
    int C[] = new int[t];
    
    
    for (int i = 0; i < t; ++i) {
      R[i] = iin.nextInt();
      C[i] = iin.nextInt();
      char M[][] = new char[R[i]][C[i]];
      for(int j=0;j<R;j++)
          for(int k=0;k<C;k++)
              M[j][k] = (char)System.in.read();
    
      for(int j=0;j<R;j++)
          for(int k=0;k<C;k++){
              if (M[j][k]=='?'){
                  if(j==0 && k ==0){   // Top Left Corner
                      if(M[j][k+1]!='?' && M[j+1][k+1] != M[j][k+1]) //Right
                          M[j][k] = M[j][k+1];
                      else if(M[j+1][k]!='?' && M[j+1][k+1] != M[j+1][k]) //Bottom
                          M[j][k] = M[j+1][k];
                  }
                  
                  if(j>0 && k ==0 && j<R-1){  // 1st column
                      if(M[j][k+1]!='?' && M[j+1][k+1] != M[j][k+1] && M[j-1][k+1]!=M[j][k+1]) // Right
                          M[j][k] = M[j][k+1];
                      else if(M[j+1][k]!='?' && M[j+1][k+1] != M[j+1][k])  // Bottom
                          M[j][k] = M[j+1][k];
                      else if(M[j-1][k]!='?' && M[j-1][k+1] != M[j-1][k])   // Top
                          M[j][k] = M[j-1][k];
                  }
                  if(j==0 && k>0 && k<C-1){   // 1st Row
                      if(M[j][k+1]!='?' && M[j+1][k+1] != M[j][k+1]) // Right
                          M[j][k] = M[j][k+1];
                      else if(M[j+1][k]!='?' && M[j+1][k+1] != M[j+1][k] && M[j+1][k-1] != M[j+1][k])  // Bottom
                          M[j][k] = M[j+1][k];
                      else if(M[j][k-1]!='?' && M[j+1][k-1] != M[j][k-1])  // Left
                          M[j][k] = M[j-1][k];
                  }
                  
                  if(j>0 && k>0 && k<C-1 && j<R-1){   // Middle
                      if(M[j][k+1]!='?' && M[j+1][k+1] != M[j][k+1] && M[j-1][k+1] != M[j][k+1] && M[j][k+2] != M[j][k+1]) // Right
                          M[j][k] = M[j][k+1];
                      else if(M[j+1][k]!='?' && M[j+1][k+1] != M[j+1][k] && M[j+1][k-1] != M[j+1][k])  // Bottom
                          M[j][k] = M[j+1][k];
                      else if(M[j][k-1]!='?' && M[j+1][k-1] != M[j][k-1])  // Left
                          M[j][k] = M[j-1][k];
                  }
              }
          }
          
    }
    for(int i=0;i<t;i++){
            System.out.println("Case #" + (i+1) + ": " +Max[i]+" "+Min[i]);
    }
  }
}
