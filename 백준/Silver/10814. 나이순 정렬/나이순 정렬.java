import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Person {
    public int id;
    public int age;
    public String name;

    public Person(int id, int age, String name) {
        this.id = id;
        this.age = age;
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        List<Person> personList = new ArrayList<>();
        // 나이, 이름 입력 받아 N개의 객체로 만들고
        for (int i = 1; i < N+1; i++) {
            String[] input = br.readLine().split(" ");
            // 객체마다 생성된 순으로 id도 부여
            int id = Integer.parseInt(String.valueOf(i));
            int age = Integer.parseInt(String.valueOf(input[0]));
            String name = input[1];
            Person person = new Person(id, age, name);
            // 사람 객체 리스트에 담아서
            personList.add(person);
        }
        // 나이 오름차순, 만든 순서 오름차순 정렬
        Collections.sort(personList, (a,b) -> {
            if (a.age != b.age) {
                return a.age - b.age;
            }
            return a.id - b.id;
        });

        for (Person person : personList) {
            bw.write(person.age + " " + person.name + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
