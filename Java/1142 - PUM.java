import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int testCases = sc.nextInt(),count = 1;
	    for (int i = 1; i <= testCases; i++) {
	        System.out.printf("%d %d %d PUM%n",count,count + 1,count + 2);
	        count+=4;
        }
	}
}