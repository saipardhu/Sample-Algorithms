import java.util.ArrayList;

public class Index_TargetVal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int nums[] = {5, 7, 7, 8, 8, 10};
		int target = 8;
		ArrayList<Integer> ar = new ArrayList<Integer>();
		int low =0;
		int high = nums.length-1;
		while(low<=high){
			int mid = (low+high)/2;
			if(nums[mid]<target) low=mid+1;
			else high=mid-1;
			if(nums[mid]==target) {
				ar.add(mid);
				mid++;
			}
		}
		int res[] = new int[ar.size()];
		for(int i=0;i<ar.size();i++){
			res[i]=ar.get(i);
		}
		for(int i=0;i<res.length;i++)
		System.out.println(res[i]);

	}

}
