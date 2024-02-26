import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt(), number;
        for (int count = 0; count < cases; count++) {
            number = sc.nextInt();
            if (number == 0)
                System.out.println("NULL");
            else if (number%2!=0) {
                if (number > 0)
                    System.out.println("ODD POSITIVE");
                else    
                    System.out.println("ODD NEGATIVE");
            }
            else {
                if (number > 0)
                    System.out.println("EVEN POSITIVE");
                else    
                    System.out.println("EVEN NEGATIVE");
            }
        } 
    
    }
}
