import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        boolean[][] paper = new boolean[100][100];
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // 색종이 수

        for (int k = 0; k < n; k++) {
            int x = sc.nextInt();  // 왼쪽으로부터 거리
            int y = sc.nextInt();  // 아래쪽으로부터 거리

            // 색종이 크기만큼 true로 채우기
            for (int i = x; i < x + 10; i++) {
                for (int j = y; j < y + 10; j++) {
                    paper[i][j] = true;
                }
            }
        }

        // 검은 영역 넓이 계산
        int count = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (paper[i][j]) count++;
            }
        }

        System.out.println(count);
    }
}
