i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i_2 = int(input())
d_2 = float(input())
s_2 = input()
# Read and save an integer, double, and String to your variables.
# Print the sum of both integer variables on a new line.
print(i + i_2)

# Print the sum of the double variables on a new line.

print(d + d_2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.

print(s + s_2)
'''
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);

        /* Declare second integer, double, and String variables. */
        
        int i_2 = scan.nextInt();
        double d_2 = scan.nextDouble();
        scan.nextLine();
        String ss = scan.nextLine();

        /* Read and save an integer, double, and String to your variables.*/
        // Note: If you have trouble reading the entire String, please go back and review the Tutorial closely.
        int sum_i = i + i_2;
        double sum_d = d + d_2;
        String sum_s = s + ss;
        /* Print the sum of both integer variables on a new line. */
        System.out.println(sum_i);
        /* Print the sum of the double variables on a new line. */
		System.out.println(sum_d);
        /* Concatenate and print the String variables on a new line; 
        	the 's' variable above should be printed first. */
        System.out.println(sum_s);
        scan.close(); '''
