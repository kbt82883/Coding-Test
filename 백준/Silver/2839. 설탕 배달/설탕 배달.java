import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int cnt = 0;
        while (N != 0) {
            if (N % 5 == 0) {
                N -= 5;
                cnt++;
            } else if (N % 3 == 0) {
                N -= 3;
                cnt++;
            } else {
                if (N >= 8) {
                    N -= 5;
                } else if (N >= 3) {
                    N -= 3;
                } else {
                    System.out.println(-1);
                    return;
                }

                cnt ++;
            }
        }

        System.out.println(cnt);

    }
}
