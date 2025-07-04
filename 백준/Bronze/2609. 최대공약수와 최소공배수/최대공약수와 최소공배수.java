import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] arr = br.readLine().split(" ");
        int A = Integer.parseInt(arr[0]);
        int B = Integer.parseInt(arr[1]);

        for (int i = A; i > 0 ; i--) {
            if (A % i == 0 && B % i == 0) {
                bw.write(i + "\n");
                break;
            }
        }

        for (int i = A; i <= A*B; i++) {
            if (i % A == 0 && i % B == 0) {
                bw.write(i + "");
                break;
            }
        }


        bw.flush();
        bw.close();
        br.close();
    }
}
