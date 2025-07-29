import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        List<String[]> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            list.add(br.readLine().split(" "));
        }

        Collections.sort(list, (a, b) -> {
            int a1 = Integer.parseInt(a[0]);
            int b1 = Integer.parseInt(b[0]);
            int a2 = Integer.parseInt(a[1]);
            int b2 = Integer.parseInt(b[1]);

            if (a2 == b2) {
                return a1 - b1;
            }
            return a2 - b2;
        });

        for (int i = 0; i < N; i++) {
            bw.write(list.get(i)[0] + " " + list.get(i)[1] + "\n");

        }

        bw.flush();
        bw.close();
        br.close();
    }
}
