import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        // N번 반복해서 배열에 담고
        // 이중반복으로 전체 스캔하여, 해당 인덱스에 맞게 숫자 더해주기

        List<String> list = new ArrayList<>();
        int[] rank = new int[N];

        for (int i = 0; i < N; i++) {
            list.add(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(list.get(i).split(" ")[0]);
            int y = Integer.parseInt(list.get(i).split(" ")[1]);
            int k = 1;

            for (int j = 0; j < N; j++) {
                int p = Integer.parseInt(list.get(j).split(" ")[0]);
                int q = Integer.parseInt(list.get(j).split(" ")[1]);

                if (x < p && y < q) {
                    k++;
                }
            }

            rank[i] = k;
        }

        for (int i = 0; i < N; i++) {
            bw.write(rank[i] + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
