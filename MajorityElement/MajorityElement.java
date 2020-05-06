import java.io.IOException;

public class MajorityElement {
    
    public static int majorityElement(int[] nums) {
    	int e = 0;
    	int n = nums.length;
		return (majority(nums,(int) Math.floor(n/Math.pow(2,1)),(int) Math.floor(n/2),n,1));
    }
    
    private static int frequency(int[] nums,int n) {
		int count = 0;
		for(int i =0;i<nums.length;i++) {
			if(nums[i]==n) count+=1;
		}
		return count;
	}
    
    

	private static int majority(int[] nums,int n,int e,int m,int i) {
		if(frequency(nums,nums[n])>e) return nums[n];
		else {
			i = i+1;
			if(n==0 || n==m-1) return -1;
			if(n<=e) {
				int o = majority(nums,0+(int) Math.floor(m/Math.pow(2,i)),e,m,i);
				if (o!=-1) return o;
			}
			if(n>=e) {
				int o = majority(nums,n+(int) Math.floor(m/Math.pow(2,i)),e,m,i);
				if (o!=-1) return o;
			}
			return -1;
		}
	}
	
	
	
    public static int majorityElementBetter(int[] nums) {
        
        if (nums == null || nums.length == 0) {
            return 0;
        }
        return majorityElement(nums, 0);
    }
    private static int majorityElement(int[] nums, int start){
        int count = 1;
        int num = nums[start];
        for(int i = start+1;i<nums.length;i++){
            if(num == nums[i]) count++;
            else count--;
            if(count == 0) return majorityElement(nums,i+1);
        }
        return num;
    }
	
    
	public static void main(String[] args) throws IOException {
		int s[] = {2,2,1,3,1,1,4,1,1,5,1,1,6};
		System.out.println(majorityElement(s));
		System.out.println(majorityElementBetter(s));
	}
    
}
