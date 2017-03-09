import java.util.LinkedList;
import java.util.Queue;
public class q3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue<Integer> q = new LinkedList<Integer>();
		for(int i=1;i<=5;i++){
			q.add(i);
		}
		while(q.size()>2){
			int p= q.remove();
			int r = q.remove();
			q.add(p);
		}
		//int last = q.pop();
		int last2 = q.remove();
		System.out.print(last2);
	}

}
