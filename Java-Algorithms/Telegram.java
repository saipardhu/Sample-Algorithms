import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
public class Telegram {
	 public static void main(String args[]){
		 
	        Scanner sc = new Scanner(System.in);
//	        int counter=0;
	        String input = sc.nextLine();
	        int max = sc.nextInt();
		 	//String input = "This is a java string";
		 	//int max = 6;
	        String ary[]=input.split(" ");
	        System.out.println(Arrays.toString(ary));
	        ArrayList<String> output = new ArrayList<String>();
//	        StringBuilder sb = new StringBuilder();
	        String sb = "";
	        for(int i=0; i<ary.length;i++){
	        	//System.out.println("i" + i);
	            if(ary[i].length() +sb.length()<=max)
	            {
	                sb = sb + ary[i] + " ";
	            }
	            //else if(ary[i].length()+sb.length()>max) sb.append(ary[i]+" ");
	           else 
	        	   {
	        	   output.add(sb.trim());
	        	   i = i-1;
	        	   sb = "";
	        	   }
	        }
	        output.add(sb.trim());
	        System.out.println(output);
	        for (String str: output)
	        	System.out.println(str);
	    }  
	}

