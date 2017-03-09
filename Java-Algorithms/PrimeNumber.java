import java.util.Scanner;
public class PrimeNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n;
		boolean a = true;
		Scanner reader = new Scanner(System.in);  
		System.out.println("Enter a number: ");
		n = reader.nextInt();
		for(int i=2;i<=Math.sqrt(n);i++){
			if(n%i==0){
			 a= false;
			 break;
		}
		}
		if(a==true)
		System.out.println("Prime");
		else 
			System.out.println("Not Prime");
	}

}
