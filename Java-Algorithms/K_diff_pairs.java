/*Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
 * Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.*/
import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
public class K_diff_pairs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int nums[] = {1,2,3,4,5};
		int k = sc.nextInt();		
		K_diff_pairs fp = new K_diff_pairs();
		System.out.println(fp.findPairs(nums,k));

	}
	public int findPairs(int[] nums, int k) {
		  if (nums == null || nums.length == 0 || k < 0)   return 0;
	        
	        Map<Integer, Integer> map = new HashMap<>();
	        int count = 0;
	        for (int i : nums) {
	            map.put(i, map.getOrDefault(i, 0) + 1);
	        }
	        
	        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
	            if (k == 0) {
	                //count how many elements in the array that appear more than twice.
	                if (entry.getValue() >= 2) {
	                    count++;
	                } 
	            } else {
	                if (map.containsKey(entry.getKey() + k)) { //check if the number that complements is present in the Map
	                    count++;
	                }
	            }
	        }
	        
	        return count;
    }

}
