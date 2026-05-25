#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string toBinary(int n){

    string result = "";

    while(n > 0){

        result += to_string(n % 2);

        n /= 2;
    }

    reverse(result.begin(), result.end());

    return result;
}

vector<int> solution(string s) {

    int transform = 0;
    int removed = 0;

    while(s != "1"){

        int oneCount = 0;

        for(char c : s){

            if(c == '1'){
                oneCount++;
            }
            else{
                removed++;
            }
        }

        s = toBinary(oneCount);

        transform++;
    }

    return {transform, removed};
}