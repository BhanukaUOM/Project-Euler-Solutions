import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        long[] fib = new long[90];
        fib[1] = 1;
        fib[2] = 1;
        for(int i=2; i<90; i++){
            fib[i] = fib[i-1]+fib[i-2];
        }
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){            
            long ans = 0;
            long n = in.nextLong();
            for(int i=0; i<90; i++){
                if(fib[i]>n)
                    break;
                if(fib[i]%2==0){
                    ans+=fib[i];
                }
            }
            System.out.println(ans);
        }
        //for(int i=0; i<90; i++)
        //System.out.println(fib[i]);
    }
}
