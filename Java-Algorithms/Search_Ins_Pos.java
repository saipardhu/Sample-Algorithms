//Program that outputs the index in the array where the target number would fit if array is assumed to be in ascending order
import java.util.Arrays;
import java.util.Scanner;

public class Search_Ins_Pos {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n, target;
		//int a=0;
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		target=sc.nextInt();
		int nums[] = new int[n];
		for(int j=0;j<n;j++){
        	nums[j] = sc.nextInt();
		}
		Arrays.sort(nums);
        if(target<=nums[0]) System.out.println(0);
        else if(target>nums[n-1]) System.out.println(n); 
        else{
        for(int i=0;i<n-1;i++){
            if((nums[i]<target)&&(target<=nums[i+1]))
             System.out.println(i+1); 
        }
        }
}
}
