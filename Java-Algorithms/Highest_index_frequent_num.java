/*Given an array of integers, find the highest index of the maximum repeated value from the array. 
 * Example given array as [1,3,1,4,5,3,3] the function must return 6 as it being the max index of frequently occuring number i.e. 3. */

import java.awt.RenderingHints.Key;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Highest_index_frequent_num {
	public static void main(String[] args) {
		int nums[]={1,5,3,3,5,6,5,7};
		HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
		for(int i=0;i<nums.length;i++){
			if(hm.containsKey(nums[i])){                     
				hm.put(nums[i], hm.get(nums[i])+1);   //Storing the elements and its frequencies in the hashmap 'hm'. 
			}
			else
				hm.put(nums[i], 1);
		}
		Map.Entry<Integer, Integer> maxEntry = null;

//		for (Map.Entry<Integer, Integer> entry : hm.entrySet())
//		{
//		    if (maxEntry == null || entry.getValue().compareTo(maxEntry.getValue()) > 0)
//		    {
//		        maxEntry = entry;
//		    }
//		}
//		System.out.println(maxEntry.getKey());
		Integer freq_key = Collections.max(hm.entrySet(), Map.Entry.comparingByValue()).getKey(); // get the key associated with the highest value
		//System.out.println(freq_key);
		for(int i=nums.length-1;i>=0;i--){        // iterating through the array in reverse to get the max index of the frequent number first.
			if(nums[i]==freq_key){
				System.out.println(i);
				break;
			}
		
		}
	}
}

