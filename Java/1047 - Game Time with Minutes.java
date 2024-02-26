import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int initialHour = sc.nextInt();
        int initialMinute = sc.nextInt();
        int finalHour = sc.nextInt();
        int finalMinute = sc.nextInt();
        int hoursTime, minutesTime;

        if (initialHour == finalHour && initialMinute == finalMinute) {
            hoursTime = 24;
            minutesTime = 0;
        } else {
            minutesTime = finalMinute - initialMinute;
            if (initialHour < finalHour) {
                hoursTime = finalHour - initialHour;
            } else if (initialHour == finalHour) {
                if (minutesTime >= 0) {
                    hoursTime = 0;
                } else {
                    hoursTime = 24 - initialHour + finalHour;
                }
            } else {
                hoursTime = 24 - initialHour + finalHour;
            }

            if (minutesTime < 0) {
                minutesTime += 60;
                hoursTime -= 1;
            }
        }

        System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", hoursTime, minutesTime);
    }
}
