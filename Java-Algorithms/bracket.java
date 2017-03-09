import java.util.Stack;
public class bracket {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<Character> st = new Stack<Character>();
		char[] ch={'[','{','(',')','}',']'}; 
		boolean flag = true;
		for(int i=0;i<ch.length;i++){
			if(ch[i]=='['||ch[i]=='{'||ch[i]=='('){
				st.push(ch[i]);
			}
			else{
				if(st.empty()){
					flag = false;
					break;}
				char c = st.pop(); 
				if((ch[i]==']' && c != '[')||(ch[i]=='}' && c != '{')||(ch[i]==')' && c != '(')){
					flag = false;
					break;
					}
				
			}
				
		}
		if(!st.empty())
			flag = false;
		
		if(!flag) System.out.println("InValid order");
		else System.out.println("Valid Order");
	}

}
