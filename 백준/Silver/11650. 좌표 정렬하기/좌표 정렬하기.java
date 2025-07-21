import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        // N번 반복해서 이중 배열로 x, y를 입력 받는다
        List<int[]> matrix = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            matrix.add(new int[2]);
        }

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");

            matrix.get(i)[0] = Integer.parseInt(input[0]);
            matrix.get(i)[1] = Integer.parseInt(input[1]);
        }

        Collections.sort(matrix, (a,b) -> {
            // x좌표가 다르면 더 작은게 먼저
            if (a[0] != b[0]) {
                return a[0] - b[0];
            }
            // x좌표가 같으면, y좌표가 더 작은게 먼저
            return a[1] - b[1];
        });

        for (int i = 0; i < N; i++) {
            bw.write(matrix.get(i)[0] + " " + matrix.get(i)[1] + "\n");
        }


        bw.flush();
        bw.close();
        br.close();
    }
}
