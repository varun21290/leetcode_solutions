import java.io.IOException;

public class FirstUniqueCharacter {
    
    public static int firstUniqChar(String s) {
    	int map[] = new int[26];
    	int j = s.length();
    	for (char c : s.toCharArray()) {
    		map[c-97]+= 1;
    	}
    	for (int i = 0;i<26;i++) {
    		if(map[i]==1 && s.indexOf(i+97) < j) j = s.indexOf(i+97);
    	}
		return j==s.length()?-1:j;
    }
    
    
	public static void main(String[] args) throws IOException {
		
		String s = "leetccodel";
		System.out.println(firstUniqChar(s));
	}
    
}
