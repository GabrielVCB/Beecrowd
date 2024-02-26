import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        for (int count = 1; count < number; count+=2)
            System.out.printf("%d\n",count);
        if (number%2!=0)
            System.out.printf("%d\n",number);
    }
}
