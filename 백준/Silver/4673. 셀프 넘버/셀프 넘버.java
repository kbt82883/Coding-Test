import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int[] arr = new int[10001];
        // 1부터 10000까지 반복
        for (int i = 1; i <= 10000; i++) {
            // N = i의 각 자리수 구해서 모두 더한 값
            int sum = i;
            int k = i;
            while (k != 0) {
                sum = sum + (k % 10);
                k /= 10;
            }
            // 10000길이의 배열의 N번 인덱스에 1더하기
            if (sum <= 10000) {
                arr[sum] += 1;
            }
        }
        // 해당하는 배열의 값이 0인 인덱스 번호를 출력하는 반복문
        for (int i = 1; i <= 10000; i++) {
            if (arr[i] == 0) {
                bw.write(i + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
