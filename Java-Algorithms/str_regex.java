import java.util.regex.*;
import java.util.Scanner;
public class str_regex {
		public static void main(String [] args){
			Scanner reader = new Scanner(System.in);  
			String str = reader.next();
			String ptrn="(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)";
			//String ptrn = "\\b((25[0–5]|2[0–4]\\d|[01]?\\d\\d?)(\\.)){3}(25[0–5]|2[0–4]\\d|[01]?\\d\\d?)\\b";
			Pattern p = Pattern.compile(ptrn);
			Matcher m = p.matcher(str);
			if(m.find()==true) System.out.println(m.group()+ " is the IP address in the string.");
			else System.out.println("No IP address");
		}
		

}
