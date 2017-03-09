import java.util.Arrays;
import java.util.Scanner;
public class ProdExceptSelf {
	public static void main(String[] args){
				int n;
				Scanner sc = new Scanner(System.in);
				n=sc.nextInt();
				int nums[]= new int[n];//{1,2,3,4};
		        //int result[] = new int[n];
		        int prod=1;
		        for(int i=0;i<n;i++){
		        	nums[i] = sc.nextInt();
		            prod = prod*nums[i];
		        }
		        for (int j=0;j<n;j++){
		            nums[j]=prod/nums[j];
		            //System.out.print(result[j]+"\t ");
		        }
		        System.out.println(Arrays.toString(nums));
		        }
		    
		}
	


