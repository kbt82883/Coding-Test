import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        // 666부터 리스트에 넣으면서 1을 더하며 반복한다
        // 리스트의 길이가 N이되면, N-1번 인덱스의 숫자를 출력한다
        int a = 666;
        List<Integer> list = new ArrayList<Integer>();
        while (list.size() < N) {
            if (String.valueOf(a).contains("666")) {
                list.add(a);
            }
            a++;
        }

        bw.write(String.valueOf(a-1));

        bw.flush();
        bw.close();
        br.close();
    }
}
