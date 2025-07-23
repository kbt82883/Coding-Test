import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int X = Integer.parseInt(br.readLine());

        // 1번째는 1/1, 총합 2
        int left = 1;
        int right = 1;

        int flag = 1;
        // X번 반복
        for (int i = 1; i < X; i++) {
            // flag가 1이면, 총합을 더하고
            if (flag == 1) {
                // 만약 왼쪽이 1이면, 오른쪽 +1, 총합도 +1
                // 만약 오른쪽이 1이면, 왼쪽 +1, 총합도 +1
                if (left == 1) {
                    right++;
                    flag = 2;
                } else if (right == 1) {
                    left++;
                    flag = 3;
                }
            }else if (flag == 2) {  // flag가 2이면, 왼쪽이 커지고 오른쪽이 작아지고
                left++;
                right--;
                if (right == 1) {
                    flag = 1;
                }
            }else if (flag == 3) {  // flag가 3이면, 오른쪽이 커지고 왼쪽이 작아지고
                right++;
                left--;
                if (left == 1) {
                    flag = 1;
                }
            }
        }

        bw.write(left + "/" + right);


        bw.flush();
        bw.close();
        br.close();
    }
}
