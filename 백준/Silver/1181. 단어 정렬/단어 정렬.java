import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        Set<String> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }

        List<String> list = new ArrayList<>(set);

        Collections.sort(list, (s1,s2) -> {
            //길이가 짧은 것부터, 길이가 같으면 알파벳 순서로
            if (s1.length() != s2.length()) {
                return s1.length() - s2.length();
            }
            return s1.compareTo(s2);
        });

        for (int i = 0; i < list.size(); i++) {
            bw.write(list.get(i));
            bw.newLine();
        }


        bw.flush();
        bw.close();
        br.close();
    }
}
