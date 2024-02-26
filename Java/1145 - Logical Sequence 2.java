import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numbersPline = sc.nextInt(), testCases = sc.nextInt(), count = 1;
        for (int i = 1; count <= testCases; i++) {
            for (int j = 0; j < numbersPline; j++) {
                System.out.print(count);
                if (j < numbersPline - 1) {
                    System.out.print(" ");
                }
                count++;
            }
            System.out.println("");
        }
    }
}
