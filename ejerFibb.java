import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.*;

class Main{
    public static void main(String [] args){
        Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		
		for(int i = 0; i<t; i++){
            
            BigInteger niNum = new BigInteger();
		    long m = in.nextLong();
		    long sobrev = (calcularFibonacci(m) % 10);
		    System.out.println(sobrev);
		}
		
	}
	
	static BigDecimal calcularFibonacci(long n){
	    ArrayList<Long> arr = new ArrayList<>();
        arr.add((long)0);
        arr.add((long)1);
        arr.add((long)2);
        
        for(int i = 3; i<arr.size(); i++){
            arr.add(arr.get(i-1)+arr.get(i-2));
        }
        
        return 1;
    }
    
}