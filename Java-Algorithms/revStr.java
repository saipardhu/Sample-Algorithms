
public class revStr {
	 public boolean isPalindrome(int x) {
	        String y = Integer.toString(x); int l=0;
	        if(y.charAt(0)=='-') l=1;
	        String n = "";
	        for(int i=y.length()-1;i>=l;i--)
	        n = n + y.charAt(i);
	        if(n.equals(y)){
	          return true;  
	        }
	        else return false;
	    }
	 public static void main(String[] args) {
			// TODO Auto-generated method stub
			revStr is = new revStr();
			is.isPalindrome(2001);
			if(true) System.out.println("Palindrome");
			else System.out.println("Not Palindrome");

		}

}
