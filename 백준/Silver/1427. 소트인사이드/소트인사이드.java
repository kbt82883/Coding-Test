import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        List<Integer> list = new ArrayList<>();

        while (N != 0) {
            list.add(N % 10);
            N /= 10;
        }

        Collections.sort(list, (a,b) -> b - a);

        for (int i = 0; i < list.size(); i++) {
            bw.write(list.get(i) + "");
        }


        bw.flush();
        bw.close();
        br.close();
    }
}
