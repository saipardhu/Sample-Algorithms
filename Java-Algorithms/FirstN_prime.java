import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class FirstN_prime {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int max, counter =0, primeCnt = 0;
		//boolean a = true;
		Scanner reader = new Scanner(System.in);  
		System.out.println("Enter a number: ");
		max = reader.nextInt();
		//for (int i = 2; i <= max; i++) {
		for (int i = 2; primeCnt <max; i++) {
			counter = 0;
		    for (int n = 2; n < i; n++) {
		        if (i % n == 0) {
		            counter++;
		        }
		    }
		    if (counter == 0) {
		        System.out.println(i);
		        primeCnt++;
		    }

		}
	}
	}

