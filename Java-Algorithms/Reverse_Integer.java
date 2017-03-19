/*Program to reverse a signed integer value. If the reversed value is greater than the 32-bit signed integer value, returns 0*/
import java.util.Scanner;
public class Reverse_Integer {
	  public int reverse(int x) {
		  long reverse= 0;
	        while( x != 0){
	            reverse= reverse*10 + x % 10;
	            x= x/10;
	        }
	            if( reverse > Integer.MAX_VALUE || reverse < Integer.MIN_VALUE) // Check if the value reversed is not greater than the 32-bit integer value
	                return 0;
	            else return (int) reverse;
	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		Reverse_Integer rv= new Reverse_Integer();
		System.out.println(rv.reverse(x));

	}

}
