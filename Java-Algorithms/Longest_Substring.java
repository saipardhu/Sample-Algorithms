//Program to find the longest substring without repeating characters 
import java.util.ArrayList;
import java.util.Scanner;
class Longest_Substring{
	public static void main(String[] args) {
		// TODO Auto-generated method stub 
		Scanner sc = new Scanner(System.in);
		ArrayList<String> output = new ArrayList<String>();
		String n =" ";
		String s = sc.next();
		if(s.isEmpty()){
		    System.out.println(0); 
		}
		else if(s.length()==1) System.out.println(1);
		else{
		for(int i=0;i<s.length();i++){
			char c = s.charAt(i);
			if(n.indexOf(c)==-1){ //indexOf returns -1 if no char contains in the string, else returns the index of char in string i.e if n doesnt contain c
				n+=c;
			}
			else if(n.indexOf(c)>0){//if n contains c
				output.add(n.trim());
				n=" ";
				n+=c;	
			}
			
		}
		output.add(n.trim());
		int max = output.get(0).length(); //ArrayList.get() used to index the ArrayList
		int index=0;
		for(int i=1;i<output.size();i++){
			if(max<output.get(i).length()){
				max=output.get(i).length();
				index=i;
			}
	}
		System.out.println("Longest Substring is:"+ output.get(index)+",having the length:"+ (max));
		}
}
}