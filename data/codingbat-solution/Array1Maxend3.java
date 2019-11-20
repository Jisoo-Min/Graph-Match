class Array1Maxend3{ 
/* Given an array of ints length 3, figure out which is larger between the 
 * first and last elements in the array, and set all the other elements to be 
 * that value. Return the changed array.
 */
public int[] maxEnd3(int[] nums) {
	int max;

	if(nums[0] > nums[2]){
		max = nums[0];
	}else{
		max = nums[1];
	}
	
	nums[0] = max;
	nums[1] = max;
	nums[2] = max;
            

	return nums;
}
}
